#!/usr/bin/env python3

import os, re, subprocess
import argparse, configparser
import base64, yaml
import geoip2.database


def convert(subscription,target,other_config={'deduplicate':False,'rename':'','include':'','exclude':'','config':''}):
    """Wrapper for subconverter
    subscription: subscription url or content string or local file path, add url support.
    target: target subconvert configuration
    other_config:
        deduplicate: whether to deduplicate
        include: include string in remark
        exclude: exclude string in remark
        config: output subcription config
    """
    config = {'target':target,'deduplicate':other_config['deduplicate'],'rename':other_config['rename'],'include':other_config['include'],'exclude':other_config['exclude'],'config':other_config['config']}

    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if subscription[:8] == 'https://':
        clash_provider = subconverterhandler(subscription)
    else:
        try:
            with open(subscription, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'proxies:' not in content and '://' in content:
                    subscription = content
                    raise ValueError
                else:
                    clash_provider = subconverterhandler(subscription)
        except Exception:
            try:
                if 'proxies:' not in subscription:
                    if '://' in subscription:
                        subscription = base64_encode(subscription)
                        with open('./subscription', 'w', encoding='utf-8') as f:
                            f.write(subscription)
                        clash_provider = subconverterhandler('./subscription')
                        os.remove('./subscription')
                else:
                    with open('./subscription', 'w', encoding='utf-8') as f:
                        f.write(subscription)
                    clash_provider = subconverterhandler('./subscription')
                    os.remove('./subscription')
            except Exception:
                print('No nodes were found in url.')
                os.chdir(work_dir)
                return ''

    if config['deduplicate']:
        clash_provider = deduplicate(clash_provider)

    with open('./temp', 'w', encoding= 'utf-8') as temp_file:
        temp_file.write(clash_provider)
    output = subconverterhandler('./temp',config)
    os.chdir(work_dir)
    return output

def subconverterhandler(subscription,input_config={'target':'clash_provider','rename':'','include':'','exclude':'','config':''}):
    """Wrapper for subconverter(by configuration file: generate.ini)
    Target handling config parameters(parameters from https://github.com/tindy2013/subconverter/blob/master/README-cn.md#%E8%BF%9B%E9%98%B6%E9%93%BE%E6%8E%A5):
        target: target subconvert configuration
        url: input subcription url or file path
        include: include string in remark
        exclude: exclude string in remark
        config: output subcription config
    Function input_config variant should be a dictionary which has keys and values of above parameters, output content will be string of target configuration.
    By default, functon will output clash_provider without any format methods.
    """
    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    configparse = configparser.ConfigParser()
    configparse.read('./generate.ini')

    url = subscription
    target = input_config['target']
    rename = input_config['rename']
    include = input_config['include']
    exclude = input_config['exclude']
    config = input_config['config']
    configparse.set(target,'url',url)
    configparse.set(target,'rename',rename)
    configparse.set(target,'include',include)
    configparse.set(target,'exclude',exclude)
    configparse.set(target,'config',config)

    with open('./generate.ini', 'w', encoding='utf-8') as ini:
        configparse.write(ini,space_around_delimiters=False)

    if os.name == 'posix':
        args = ['./subconverter-linux-amd64', '-g', '--artifact', target]
    elif os.name == 'nt':
        args = ['.\subconverter-windows-amd64.exe', '-g', '--artifact', target]
    subconverter = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True,encoding='utf-8',bufsize=1)
    logs = subconverter.stdout.readlines()
    subconverter.wait()
    # Print log
    pre_run = False
    for line in logs:
        if 'Fetching node data from url' in line and '\'./temp\'' not in line:
            pre_run = True
            print(line[:-1])
    if pre_run == False:
        if '[INFO]' not in (logs[-3]):
            print(logs[-2])
        else:
            print(logs[-3])

    if subconverter.returncode != 0:
        try:
            os.remove('./temp')
            os.chdir(work_dir)
            return ''
        except Exception:
            os.chdir(work_dir)
            return ''
    else:
        try:
            with open(f'./temp', 'r', encoding= 'utf-8', errors='ignore') as temp_file:
                output = ''
                while True:
                    content = temp_file.read(100)
                    if not content:
                        break
                    output += content
            if target == 'url':
                output = base64_decode(output)

            os.remove('./temp')
            os.chdir(work_dir)
            return output
        except Exception:
            os.chdir(work_dir)
            return ''
def deduplicate(clash_provider): # Proxies deduplicate. If proxies have same servers that are greater than 4 then just save 4 of them, else less than 4 just save all of them.
    lines = re.split(r'\n+', clash_provider)[1:]
    print('Starting deduplicate...')
    print(f'Init amount: {len(lines)}')
    try:
        proxies = yaml.safe_load(clash_provider)['proxies'] # load all proxies from clash provider
    except Exception:
        il_chars = ['|', '?', '[', ']', '@', '!', '%', ':']

        line_fixed = ['proxies:']
        for line in lines:
            try_load = 'proxies:\n' + line
            try:
                yaml.safe_load(try_load)
                line_fixed.append(line)
            except Exception:
                value_list = re.split(r': |, ', line)
                if len(value_list) > 6:
                    value_list_fix = []
                    for value in value_list:
                        for char in il_chars:
                            value_il = False
                            if char in value:
                                value_il = True
                                break
                        if value_il == True and ('{' not in value and '}' not in value):
                            value = '"' + value + '"'
                            value_list_fix.append(value)
                        elif value_il == True and '}' in value:
                            if '}}}' in value:
                                host_part = value.replace('}}}','')
                                host_value = '"'+host_part+'"}}}'
                                value_list_fix.append(host_value)
                            elif '}}' not in value:
                                host_part = value.replace('}','')
                                host_value = '"'+host_part+'"}'
                                value_list_fix.append(host_value)
                        else:
                            value_list_fix.append(value)
                        line_fix = line
                    for index in range(len(value_list_fix)):
                        line_fix = line_fix.replace(value_list[index], value_list_fix[index])
                elif len(value_list) == 2:
                    value_list_fix = []
                    for value in value_list:
                        for char in il_chars:
                            value_il = False
                            if char in value:
                                value_il = True
                                break
                        if value_il == True:
                            value = '"' + value + '"'
                        value_list_fix.append(value)
                    line_fix = line
                    for index in range(len(value_list_fix)):
                        line_fix = line_fix.replace(value_list[index], value_list_fix[index])
                try:
                    try_load = 'proxies:\n' + line_fix
                    line_fixed.append(line_fix)
                except Exception:
                    pass
        fix_provider = '\n'.join(line_fixed)
        
        try:
            proxies = yaml.safe_load(fix_provider)['proxies']
        except Exception:
            print('Deduplicate failed, skip')
            output = clash_provider
            return output
    
    servers = {}
    for proxy in proxies:
        server = proxy['server'] # assign remote server

        if server in servers:
            servers[server].append(proxy) # add proxy to its remote server list
        elif server not in servers:
            servers[server] = [proxy] # init remote server list, add first proxy

    proxies = []
    for server in servers:
        if len(servers[server]) > 3: # if proxy amount is greater than 4 then just add 4 proxies
            add_list = servers[server][:3]
            for add in add_list:
                proxies.append(add)
        else:
            add_list = servers[server] # if proxy amount is less than 4 then add all proxies
            for add in add_list:
                proxies.append(add)
    
    print('Dedupicate success.')
    print(f'Output amount: {len(proxies)}')
    output = yaml.dump({'proxies': proxies}, default_flow_style=False, sort_keys=False, allow_unicode=True, indent=2)
    return output

def base64_decode(content):
    if '-' in content:
        content = content.replace('-', '+')
    if '_' in content:
        content = content.replace('_', '/')
    #print(len(url_content))
    missing_padding = len(content) % 4
    if missing_padding != 0:
        content += '='*(4 - missing_padding) # 不是4的倍数后加= https://www.cnblogs.com/wswang/p/7717997.html
    try:
        base64_content = base64.b64decode(content.encode('utf-8')).decode('utf-8','ignore') # https://www.codenong.com/42339876/
        base64_content_format = base64_content
        return base64_content_format
    except UnicodeDecodeError:
        base64_content = base64.b64decode(content)
        base64_content_format = base64_content
        return str(base64_content)
def base64_encode(content):
    if content == None:
        content = ''
    base64_content = base64.b64encode(content.encode('utf-8')).decode('ascii')
    return base64_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert between various proxy subscription formats using Subconverter.')
    parser.add_argument('--subscription', '-s', help='Your subscription url or local file path.', required=True)
    parser.add_argument('--target', '-t', help='Target convert format, support base64, clash, clash_provider, quanx.', default='clash')
    parser.add_argument('--output', '-o', help='Target path to output, default value is the Subconverter root directionary.', default='./Eternity.yaml')
    parser.add_argument('--deduplicate', '-d', help='Whether to deduplicate proxies, default value is False.', default=False)
    args = parser.parse_args()

    subscription = args.subscription
    target = args.target
    output_dir = args.output
    deduplicate_enabled = bool(args.deduplicate)

    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    generate = configparser.ConfigParser()
    generate.read('./generate.ini')
    config={'deduplicate': deduplicate_enabled,'rename': generate.get(target,'rename'), 'include': generate.get(target,'include'), 'exclude': generate.get(target,'exclude'), 'config': generate.get(target,'config')}

    output = convert(subscription,target,config)

    with open(output_dir, 'w', encoding= 'utf-8') as temp_file:
        temp_file.write(output)
    os.chdir(work_dir)