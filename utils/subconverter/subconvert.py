#!/usr/bin/env python3

import os, argparse, configparser
import yaml, json, base64
import geoip2.database


def subconverter(subcription,target,other_config={'deduplicate': False, 'rename': '', 'include': '', 'exclude': '', 'config': ''}):
    config = {'target':target, 'deduplicate':other_config['deduplicate'], 'rename': '', 'include':other_config['include'], 'exclude':other_config['exclude'], 'config':other_config['config']}
    
    clash_provider = subconverterhandler(subcription)
    if config['deduplicate']:
        clash_provider = node_deduplicate(clash_provider)

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('./temp', 'w', encoding= 'utf-8') as temp_file:
        temp_file.write(clash_provider)
    output = subconverterhandler('./temp',config)
    return output

def subconverterhandler(subcription,input_config={'target':'clash_provider','rename':'','include':'','exclude':'','config':''}):
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

    url = subcription
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
        os.system(f'./subconverter-linux-amd64 -g --artifact \"{target}\"')
    elif os.name == 'nt':
        os.system(f'.\subconverter-windows-amd64.exe -g --artifact \"{target}\"')

    with open(f'./temp', 'r', encoding= 'utf-8') as temp_file:
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

def node_deduplicate(clash_provider):
    # WIP
    return clash_provider

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

    configparse = configparser.ConfigParser()
    configparse.read('./generate.ini')
    config={'deduplicate': deduplicate_enabled,'rename': configparse.get(target,'rename'), 'include': configparse.get(target,'include'), 'exclude': configparse.get(target,'exclude'), 'config': configparse.get(target,'config')}

    output = subconverter(subscription,target,config)

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open(output_dir, 'w', encoding= 'utf-8') as temp_file:
        temp_file.write(output)