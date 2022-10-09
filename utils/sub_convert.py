#!/usr/bin/env python3

import re, os, argparse
import yaml, json, base64
import requests, socket, urllib.parse
import geoip2.database

#config: dup_rm_enabled, rename_enabled, rename_format, output_path

class format():
    def __init__(self,content='',config={'duplicate_remove': False, 'format_remarks': ''}):
        self.content = content
        self.config = config
        self.output = self.main()

    def main(self):
        if self.content[:8] == 'https://' and '|http' in self.content:
            urls = re.split('\|',self.content)
            content_list = []
            for url in urls:
                self.content = url
                proxies = self.makeup(self.getconfig())
                output = self.config2url(proxies)
                content_list.append(output)
            output = ''.join(content_list)
        else:
            proxies = self.makeup(self.getconfig())
            output = self.config2url(proxies)
        return format.base64_encode(output)
    def getconfig(self): # 输入订阅链接或订阅内容，得到节点配置列表
        if self.content[:8] == 'https://': # 获取 URL 订阅链接内容
            try:
                s = requests.Session()
                print('Downloading from: ' + self.content)
                resp = s.get(self.content, timeout=5)
                content = resp.content.decode('utf-8')
                node_config = self.parse(content)
                return node_config
            except Exception:
                print('Problem occurs when fetching config')
                return []
        else:
            try:
                with open(self.content, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                content = self.content
            node_config = self.parse(content)
            return node_config
    def parse(self,sub_content): # 解析订阅内容, 输出节点配置列表
        if 'proxies:' not in sub_content: # 对 URL 内容进行格式化处理
            try:
                if '://' not in sub_content:
                    sub_content = format.base64_decode(sub_content)

                raw_url_list = re.split(r'\r?\n+', sub_content)
                url_list = []
                for url in raw_url_list:
                    while len(re.split('ss://|ssr://|vmess://|trojan://|vless://', url)) > 2:
                        url_to_split = url[8:]
                        if 'ss://' in url_to_split and 'vmess://' not in url_to_split and 'vless://' not in url_to_split:
                            url_splited = url_to_split.replace('ss://', '\nss://', 1) # https://www.runoob.com/python/att-string-replace.html
                        elif 'ssr://' in url_to_split:
                            url_splited = url_to_split.replace('ssr://', '\nssr://', 1)
                        elif 'vmess://' in url_to_split:
                            url_splited = url_to_split.replace('vmess://', '\nvmess://', 1)
                        elif 'trojan://' in url_to_split:
                            url_splited = url_to_split.replace('trojan://', '\ntrojan://', 1)
                        elif 'vless://' in url_to_split:
                            url_splited = url_to_split.replace('vless://', '\nvless://', 1)
                        url_split = url_splited.split('\n')

                        front_url = url[:8] + url_split[0]
                        url_list.append(front_url)
                        url = url_split[1]

                    url_list.append(url)

                node_config = self.url2config('\n'.join(url_list))
                return node_config
            except:
                print('Problem occurs when parsing URL config.')
                return []
        elif 'proxies:' in sub_content: # 对 Clash 内容进行格式化处理
            try:
                try_load = yaml.safe_load(sub_content)
                node_config = try_load['proxies']
                return node_config
            except Exception:
                try:
                    sub_content = sub_content.replace('\'', '').replace('"', '')
                    url_list = []
                    il_chars = ['|', '?', '[', ']', '@', '!', '%', ':']
                    lines = re.split(r'\n+', sub_content)
                    line_fix_list = []
                    for line in lines:
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
                            line_fix_list.append(line_fix)
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
                            line_fix_list.append(line_fix)
                        elif len(value_list) == 1:
                            if ':' in line:
                                line_fix_list.append(line)
                        else:
                            line_fix_list.append(line)

                    sub_content = '\n'.join(line_fix_list)
                    node_config = yaml.safe_load(sub_content)
                    return node_config['proxies']
                except:
                    print('Problem occurs when parsing Clash config.')
                    return []
        else:
            print('No node found in input config.')
            return []
    def url2config(self,url_content): # 将 URL 内容转换为节点配置列表
        url_list = []

        lines = re.split(r'\n+', url_content)

        for line in lines:
            yaml_url = {}
            if 'vmess://' in line:
                try:
                    vmess_json_config = json.loads(format.base64_decode(line.replace('vmess://', '')))
                    vmess_default_config = {
                        'v': 'Vmess Node', 'ps': 'Vmess Node', 'add': '0.0.0.0', 'port': 0, 'id': '',
                        'aid': 0, 'scy': 'auto', 'net': '', 'type': '', 'host': vmess_json_config['add'], 'path': '/', 'tls': ''
                    }
                    vmess_default_config.update(vmess_json_config)
                    vmess_config = vmess_default_config

                    yaml_url = {}
                    #yaml_config_str = ['name', 'server', 'port', 'type', 'uuid', 'alterId', 'cipher', 'tls', 'skip-cert-verify', 'network', 'ws-path', 'ws-headers']
                    #vmess_config_str = ['ps', 'add', 'port', 'id', 'aid', 'scy', 'tls', 'net', 'host', 'path']
                    # 生成 yaml 节点字典
                    if vmess_config['id'] == '' or vmess_config['id'] is None:
                        print('节点格式错误')
                    else:
                        yaml_url.setdefault('name', urllib.parse.unquote(str(vmess_config['ps'])))
                        yaml_url.setdefault('server', vmess_config['add'])
                        yaml_url.setdefault('port', int(vmess_config['port']))
                        yaml_url.setdefault('type', 'vmess')
                        yaml_url.setdefault('uuid', vmess_config['id'])
                        yaml_url.setdefault('alterId', int(vmess_config['aid']))
                        yaml_url.setdefault('cipher', vmess_config['scy'])
                        yaml_url.setdefault('skip-cert-verify', True)
                        if vmess_config['net'] == '' or vmess_config['net'] is False or vmess_config['net'] is None:
                            yaml_url.setdefault('network', 'tcp')
                        else:
                            yaml_url.setdefault('network', vmess_config['net'])
                        if vmess_config['net'] == 'h2' or vmess_config['net'] == 'grpc':
                            yaml_url.setdefault('tls', True)
                        elif vmess_config['tls'] == '' or vmess_config['tls'] is False or vmess_config['tls'] is None:
                            yaml_url.setdefault('tls', False)
                        else:
                            yaml_url.setdefault('tls', True)
                        yaml_url.setdefault('ws-opts', {})
                        if vmess_config['path'] == '' or vmess_config['path'] is False or vmess_config['path'] is None:
                            yaml_url['ws-opts'].setdefault('path', '/')
                        else:
                            yaml_url['ws-opts'].setdefault('path', vmess_config['path'])
                        if vmess_config['host'] == '':
                            yaml_url['ws-opts'].setdefault('headers', {'Host': vmess_config['add']})
                        else:
                            yaml_url['ws-opts'].setdefault('headers', {'Host': vmess_config['host']})

                        url_list.append(yaml_url)
                except Exception as err:
                    print(f'yaml_encode 解析 vmess 节点发生错误: {err}')
                    pass

            if 'ss://' in line and 'vless://' not in line and 'vmess://' not in line:
                if '#' not in line:
                    line = line + '#SS%20Node'
                try:
                    ss_content =  line.replace('ss://', '')
                    part_list = ss_content.split('#', 1) # https://www.runoob.com/python/att-string-split.html
                    yaml_url.setdefault('name', urllib.parse.unquote(part_list[1]))
                    if '@' in part_list[0]:
                        mix_part = part_list[0].split('@', 1)
                        method_part = format.base64_decode(mix_part[0])
                        server_part = f'{method_part}@{mix_part[1]}'
                    else:
                        server_part = format.base64_decode(part_list[0])

                    server_part_list = server_part.split(':', 1) # 使用多个分隔符 https://blog.csdn.net/shidamowang/article/details/80254476 https://zhuanlan.zhihu.com/p/92287240
                    method_part = server_part_list[0]
                    server_part_list = server_part_list[1].rsplit('@', 1)
                    password_part = server_part_list[0]
                    server_part_list = server_part_list[1].split(':', 1)

                    yaml_url.setdefault('server', server_part_list[0])
                    yaml_url.setdefault('port', server_part_list[1])
                    yaml_url.setdefault('type', 'ss')
                    yaml_url.setdefault('cipher', method_part)
                    yaml_url.setdefault('password', password_part)

                    url_list.append(yaml_url)
                except Exception as err:
                    print(f'yaml_encode 解析 ss 节点发生错误: {err}')
                    pass

            if 'ssr://' in line:
                try:
                    ssr_content = format.base64_decode(line.replace('ssr://', ''))
                
                    parts = re.split(':', ssr_content)
                    if len(parts) != 6:
                        print('SSR 格式错误: %s' % ssr_content)
                    password_and_params = parts[5]
                    password_and_params = re.split('/\?', password_and_params)
                    password_encode_str = password_and_params[0]
                    params = password_and_params[1]

                    param_parts = re.split('\&', params)
                    param_dic = {'remarks': 'U1NSIE5vZGU=','obfsparam': '','protoparam': '','group': ''}
                    for part in param_parts:
                        key_and_value = re.split('\=', part)
                        param_dic.update({key_and_value[0]: key_and_value[1]})
                    yaml_url.setdefault('name', format.base64_decode(param_dic['remarks']))
                    yaml_url.setdefault('server', parts[0])
                    yaml_url.setdefault('port', parts[1])
                    yaml_url.setdefault('type', 'ssr')
                    yaml_url.setdefault('cipher', parts[3])
                    yaml_url.setdefault('password', format.base64_decode(password_encode_str))
                    yaml_url.setdefault('obfs', parts[4])
                    yaml_url.setdefault('protocol', parts[2])
                    yaml_url.setdefault('obfsparam', format.base64_decode(param_dic['obfsparam']))
                    yaml_url.setdefault('protoparam', format.base64_decode(param_dic['protoparam']))
                    yaml_url.setdefault('group', format.base64_decode(param_dic['group']))

                    url_list.append(yaml_url)
                except Exception as err:
                    print(f'yaml_encode 解析 ssr 节点发生错误: {err}')
                    pass

            if 'trojan://' in line:
                try:
                    url_content = line.replace('trojan://', '')
                    part_list = re.split('#', url_content, maxsplit=1) # https://www.runoob.com/python/att-string-split.html
                    yaml_url.setdefault('name', urllib.parse.unquote(part_list[1]))

                    server_part = part_list[0].replace('trojan://', '')
                    server_part_list = re.split(':|@|\?|&', server_part) # 使用多个分隔符 https://blog.csdn.net/shidamowang/article/details/80254476 https://zhuanlan.zhihu.com/p/92287240
                    yaml_url.setdefault('server', server_part_list[1])
                    yaml_url.setdefault('port', server_part_list[2])
                    yaml_url.setdefault('type', 'trojan')
                    yaml_url.setdefault('password', server_part_list[0])
                    server_part_list = server_part_list[3:]

                    for config in server_part_list:
                        if 'sni=' in config:
                            yaml_url.setdefault('sni', config[4:])
                        elif 'allowInsecure=' in config or 'tls=' in config:
                            if config[-1] == 0:
                                yaml_url.setdefault('tls', False)
                        elif 'type=' in config:
                            if config[5:] != 'tcp':
                                yaml_url.setdefault('network', config[5:])
                        elif 'path=' in config:
                            yaml_url.setdefault('ws-path', config[5:])
                        elif 'security=' in config:
                            if config[9:] != 'tls':
                                yaml_url.setdefault('tls', False)

                    yaml_url.setdefault('skip-cert-verify', True)

                    url_list.append(yaml_url)
                except Exception as err:
                    print(f'yaml_encode 解析 trojan 节点发生错误: {err}')
                    pass

        return url_list
    def makeup(self,proxies): # 输入节点列表, 对节点进行区域的筛选和重命名，输出格式化后的节点列表
        config = self.config

        vmess_config_template = {
            'name': 'Vmess Node', 'server': '127.0.0.1', 'port': 443, 'type': 'vmess', 'country': '🇺🇸US', 'uuid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
            'alterId': 0, 'cipher': 'auto', 'tls': True, 'skip-cert-verify': True, 'network': 'ws', 
            'ws-opts': {'path': '/', 'headers': {'Host': '127.0.0.1'}}, 'udp': True
        }
        ss_config_template = {
            'name': 'SS Node', 'server':'127.0.0.1', 'port':50000, 'type':'ss', 'country':'🇺🇸US', 'password':'xxxxxxxxxx', 'cipher':'aes-256-gcm'
        }
        ssr_config_template = {
            'name':'SSR Node', 'server':'127.0.0.1', 'port':8099, 'type':'ssr', 'country':'🇺🇸US', 'password':'xxxxxxxxxxxxxxxx', 'cipher':'aes-256-cfb', 'protocol':'origin', 'obfs':'plain'
        }
        trojan_config_template = {
            'name':'Trojan Node', 'server':'127.0.0.1', 'port':443, 'type':'trojan', 'country':'🇺🇸US', 'password':'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'skip-cert-verify': True, 'udp': True
        }

        flags = {
            'AD': '🇦🇩', 'AE': '🇦🇪', 'AF': '🇦🇫', 'AG': '🇦🇬', 
            'AI': '🇦🇮', 'AL': '🇦🇱', 'AM': '🇦🇲', 'AO': '🇦🇴', 
            'AQ': '🇦🇶', 'AR': '🇦🇷', 'AS': '🇦🇸', 'AT': '🇦🇹', 
            'AU': '🇦🇺', 'AW': '🇦🇼', 'AX': '🇦🇽', 'AZ': '🇦🇿', 
            'BA': '🇧🇦', 'BB': '🇧🇧', 'BD': '🇧🇩', 'BE': '🇧🇪', 
            'BF': '🇧🇫', 'BG': '🇧🇬', 'BH': '🇧🇭', 'BI': '🇧🇮', 
            'BJ': '🇧🇯', 'BL': '🇧🇱', 'BM': '🇧🇲', 'BN': '🇧🇳', 
            'BO': '🇧🇴', 'BQ': '🇧🇶', 'BR': '🇧🇷', 'BS': '🇧🇸', 
            'BT': '🇧🇹', 'BV': '🇧🇻', 'BW': '🇧🇼', 'BY': '🇧🇾', 
            'BZ': '🇧🇿', 'CA': '🇨🇦', 'CC': '🇨🇨', 'CD': '🇨🇩', 
            'CF': '🇨🇫', 'CG': '🇨🇬', 'CH': '🇨🇭', 'CI': '🇨🇮', 
            'CK': '🇨🇰', 'CL': '🇨🇱', 'CM': '🇨🇲', 'CN': '🇨🇳', 
            'CO': '🇨🇴', 'CR': '🇨🇷', 'CU': '🇨🇺', 'CV': '🇨🇻', 
            'CW': '🇨🇼', 'CX': '🇨🇽', 'CY': '🇨🇾', 'CZ': '🇨🇿', 
            'DE': '🇩🇪', 'DJ': '🇩🇯', 'DK': '🇩🇰', 'DM': '🇩🇲', 
            'DO': '🇩🇴', 'DZ': '🇩🇿', 'EC': '🇪🇨', 'EE': '🇪🇪', 
            'EG': '🇪🇬', 'EH': '🇪🇭', 'ER': '🇪🇷', 'ES': '🇪🇸', 
            'ET': '🇪🇹', 'EU': '🇪🇺', 'FI': '🇫🇮', 'FJ': '🇫🇯', 
            'FK': '🇫🇰', 'FM': '🇫🇲', 'FO': '🇫🇴', 'FR': '🇫🇷', 
            'GA': '🇬🇦', 'GB': '🇬🇧', 'GD': '🇬🇩', 'GE': '🇬🇪', 
            'GF': '🇬🇫', 'GG': '🇬🇬', 'GH': '🇬🇭', 'GI': '🇬🇮', 
            'GL': '🇬🇱', 'GM': '🇬🇲', 'GN': '🇬🇳', 'GP': '🇬🇵', 
            'GQ': '🇬🇶', 'GR': '🇬🇷', 'GS': '🇬🇸', 'GT': '🇬🇹', 
            'GU': '🇬🇺', 'GW': '🇬🇼', 'GY': '🇬🇾', 'HK': '🇭🇰', 
            'HM': '🇭🇲', 'HN': '🇭🇳', 'HR': '🇭🇷', 'HT': '🇭🇹', 
            'HU': '🇭🇺', 'ID': '🇮🇩', 'IE': '🇮🇪', 'IL': '🇮🇱', 
            'IM': '🇮🇲', 'IN': '🇮🇳', 'IO': '🇮🇴', 'IQ': '🇮🇶', 
            'IR': '🇮🇷', 'IS': '🇮🇸', 'IT': '🇮🇹', 'JE': '🇯🇪', 
            'JM': '🇯🇲', 'JO': '🇯🇴', 'JP': '🇯🇵', 'KE': '🇰🇪', 
            'KG': '🇰🇬', 'KH': '🇰🇭', 'KI': '🇰🇮', 'KM': '🇰🇲', 
            'KN': '🇰🇳', 'KP': '🇰🇵', 'KR': '🇰🇷', 'KW': '🇰🇼', 
            'KY': '🇰🇾', 'KZ': '🇰🇿', 'LA': '🇱🇦', 'LB': '🇱🇧', 
            'LC': '🇱🇨', 'LI': '🇱🇮', 'LK': '🇱🇰', 'LR': '🇱🇷', 
            'LS': '🇱🇸', 'LT': '🇱🇹', 'LU': '🇱🇺', 'LV': '🇱🇻', 
            'LY': '🇱🇾', 'MA': '🇲🇦', 'MC': '🇲🇨', 'MD': '🇲🇩', 
            'ME': '🇲🇪', 'MF': '🇲🇫', 'MG': '🇲🇬', 'MH': '🇲🇭', 
            'MK': '🇲🇰', 'ML': '🇲🇱', 'MM': '🇲🇲', 'MN': '🇲🇳', 
            'MO': '🇲🇴', 'MP': '🇲🇵', 'MQ': '🇲🇶', 'MR': '🇲🇷', 
            'MS': '🇲🇸', 'MT': '🇲🇹', 'MU': '🇲🇺', 'MV': '🇲🇻', 
            'MW': '🇲🇼', 'MX': '🇲🇽', 'MY': '🇲🇾', 'MZ': '🇲🇿', 
            'NA': '🇳🇦', 'NC': '🇳🇨', 'NE': '🇳🇪', 'NF': '🇳🇫', 
            'NG': '🇳🇬', 'NI': '🇳🇮', 'NL': '🇳🇱', 'NO': '🇳🇴', 
            'NP': '🇳🇵', 'NR': '🇳🇷', 'NU': '🇳🇺', 'NZ': '🇳🇿', 
            'OM': '🇴🇲', 'PA': '🇵🇦', 'PE': '🇵🇪', 'PF': '🇵🇫', 
            'PG': '🇵🇬', 'PH': '🇵🇭', 'PK': '🇵🇰', 'PL': '🇵🇱', 
            'PM': '🇵🇲', 'PN': '🇵🇳', 'PR': '🇵🇷', 'PS': '🇵🇸', 
            'PT': '🇵🇹', 'PW': '🇵🇼', 'PY': '🇵🇾', 'QA': '🇶🇦', 
            'RE': '🇷🇪', 'RO': '🇷🇴', 'RS': '🇷🇸', 'RU': '🇷🇺', 
            'RW': '🇷🇼', 'SA': '🇸🇦', 'SB': '🇸🇧', 'SC': '🇸🇨', 
            'SD': '🇸🇩', 'SE': '🇸🇪', 'SG': '🇸🇬', 'SH': '🇸🇭', 
            'SI': '🇸🇮', 'SJ': '🇸🇯', 'SK': '🇸🇰', 'SL': '🇸🇱', 
            'SM': '🇸🇲', 'SN': '🇸🇳', 'SO': '🇸🇴', 'SR': '🇸🇷', 
            'SS': '🇸🇸', 'ST': '🇸🇹', 'SV': '🇸🇻', 'SX': '🇸🇽', 
            'SY': '🇸🇾', 'SZ': '🇸🇿', 'TC': '🇹🇨', 'TD': '🇹🇩', 
            'TF': '🇹🇫', 'TG': '🇹🇬', 'TH': '🇹🇭', 'TJ': '🇹🇯', 
            'TK': '🇹🇰', 'TL': '🇹🇱', 'TM': '🇹🇲', 'TN': '🇹🇳', 
            'TO': '🇹🇴', 'TR': '🇹🇷', 'TT': '🇹🇹', 'TV': '🇹🇻', 
            'TW': '🇹🇼', 'TZ': '🇹🇿', 'UA': '🇺🇦', 'UG': '🇺🇬', 
            'UM': '🇺🇲', 'US': '🇺🇸', 'UY': '🇺🇾', 'UZ': '🇺🇿', 
            'VA': '🇻🇦', 'VC': '🇻🇨', 'VE': '🇻🇪', 'VG': '🇻🇬', 
            'VI': '🇻🇮', 'VN': '🇻🇳', 'VU': '🇻🇺', 'WF': '🇼🇫', 
            'WS': '🇼🇸', 'XK': '🇽🇰', 'YE': '🇾🇪', 'YT': '🇾🇹', 
            'ZA': '🇿🇦', 'ZM': '🇿🇲', 'ZW': '🇿🇼', 'ZZ': '🏁'
        }
        
        work_dir = os.getcwd() # Get working directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        proxies_list = []
        for index in range(len(proxies)):
            proxy = proxies[index]
            if proxy['type'] == 'vmess':
                vmess_config_template.update(proxy)
                proxy = vmess_config_template.copy()
            elif proxy['type'] == 'ss':
                ss_config_template.update(proxy)
                proxy = ss_config_template.copy()
            elif proxy['type'] == 'ssr':
                ssr_config_template.update(proxy)
                proxy = ssr_config_template.copy()
            elif proxy['type'] == 'trojan':
                trojan_config_template.update(proxy)
                proxy = trojan_config_template.copy()

            server = proxy['server']
            if server.replace('.','').isdigit():
                ip = server
            else:
                try:
                    ip = socket.gethostbyname(server) # https://cloud.tencent.com/developer/article/1569841
                except Exception:
                    ip = server
            with geoip2.database.Reader('./Country.mmdb') as ip_reader:
                try:
                    response = ip_reader.country(ip)
                    country_code = response.country.iso_code
                    proxy['country'] = flags[country_code]+country_code
                except Exception:
                    country_code = 'ZZ'

            proxies_list.append(proxy)
        os.chdir(work_dir) # Back to work directory
        
        if self.config['duplicate_remove']: # 去重
            begin = 0
            raw_length = len(proxies_list)
            length = len(proxies_list)
            while begin < length:
                if (begin + 1) == 1:
                    print(f'\n-----去重开始-----\n起始数量{length}')
                elif (begin + 1) % 100 == 0:
                    print(f'当前基准{begin + 1}-----当前数量{length}')
                elif (begin + 1) == length and (begin + 1) % 100 != 0:
                    repetition = raw_length - length
                    print(f'当前基准{begin + 1}-----当前数量{length}\n重复数量{repetition}\n-----去重完成-----\n')
                proxy_compared = proxies_list[begin]

                begin_2 = begin + 1
                while begin_2 <= (length - 1):

                    if proxy_compared['server'] == proxies_list[begin_2]['server'] and proxy_compared['port'] == proxies_list[begin_2]['port']:
                        proxies_list.pop(begin_2)
                        length -= 1
                    begin_2 += 1
                begin += 1

        if self.config['format_remarks'] != '': # 改名
            rename_list = []
            name_format = config['rename']['format']
            for index in range(len(proxies_list)):
                proxy = proxies_list[index]
                flag = proxy['country'][:1]
                code = proxy['country'][1:4]
                address = ip
                if index >= 999:
                    proxy['name'] = f'{flag}{code}-{address}-{index:0>4d}'
                elif index <= 999 and index > 99:
                    proxy['name'] = f'{flag}{code}-{address}-{index:0>3d}'
                elif index <= 99:
                    proxy['name'] = f'{flag}{code}-{address}-{index:0>2d}'
                rename_list.append(proxy)
            proxies_list = rename_list

        return proxies_list # 输出格式化后的节点列表
    def config2url(self,proxies): # 节点配置转换为 URL 链接内容
        url_list = []
        for proxy in proxies: # 不同节点订阅链接内容 https://github.com/hoochanlon/fq-book/blob/master/docs/append/srvurl.md
            try:
                if proxy['type'] == 'vmess': # Vmess 节点提取, 由 Vmess 所有参数 dump JSON 后 base64 encode 得来。
                    yaml_default_config = {
                        'name': 'Vmess Node', 'server': '0.0.0.0', 'port': 0, 'uuid': '', 'alterId': 0,
                        'cipher': 'auto', 'network': 'ws', 'ws-opts': {'path': '/', 'headers': {'Host': proxy['server']}},
                        'tls': '', 'sni': ''
                    }

                    yaml_default_config.update(proxy)
                    proxy_config = yaml_default_config

                    vmess_value = {
                        'v': 2, 'ps': proxy_config['name'], 'add': proxy_config['server'],
                        'port': proxy_config['port'], 'id': proxy_config['uuid'], 'aid': proxy_config['alterId'],
                        'scy': proxy_config['cipher'], 'net': proxy_config['network'], 'type': None, 'host': proxy_config['ws-opts']['headers']['Host'],
                        'path': proxy_config['ws-opts']['path'], 'tls': proxy_config['tls'], 'sni': proxy_config['sni']
                        }

                    vmess_raw_proxy = json.dumps(vmess_value, sort_keys=False, indent=2, ensure_ascii=False)
                    vmess_proxy = str('vmess://' + format.base64_encode(vmess_raw_proxy) + '\n')
                    url_list.append(vmess_proxy)

                elif proxy['type'] == 'ss': # SS 节点提取, 由 ss_base64_decoded 部分(参数: 'cipher', 'password', 'server', 'port') Base64 编码后 加 # 加注释(URL_encode)
                    ss_base64_decoded = str(proxy['cipher']) + ':' + str(proxy['password']) + '@' + str(proxy['server']) + ':' + str(proxy['port'])
                    ss_base64 = format.base64_encode(ss_base64_decoded)
                    ss_proxy = str('ss://' + ss_base64 + '#' + str(urllib.parse.quote(proxy['name'])) + '\n')
                    url_list.append(ss_proxy)

                elif proxy['type'] == 'trojan': # Trojan 节点提取, 由 trojan_proxy 中参数再加上 # 加注释(URL_encode) # trojan Go https://p4gefau1t.github.io/trojan-go/developer/url/
                    if 'tls' in proxy.keys() and 'network' in proxy.keys():
                        if proxy['tls'] == True and proxy['network'] != 'tcp':
                            network_type = proxy['network']
                            trojan_go = f'?security=tls&type={network_type}&headerType=none'
                        elif proxy['tls'] == False and proxy['network'] != 'tcp':
                            trojan_go = f'??allowInsecure=0&type={network_type}&headerType=none'
                    else:
                        trojan_go = '?allowInsecure=1'
                    if 'sni' in proxy.keys():
                        trojan_go = trojan_go+'&sni='+proxy['sni']
                    trojan_proxy = str('trojan://' + str(proxy['password']) + '@' + str(proxy['server']) + ':' + str(proxy['port']) + trojan_go + '#' + str(urllib.parse.quote(proxy['name'])) + '\n')
                    url_list.append(trojan_proxy)
                
                elif proxy['type'] == 'ssr': # ssr 节点提取, 由 ssr_base64_decoded 中所有参数总体 base64 encode
                    ssr_default_config = {}
                    remarks = format.base64_encode(proxy['name']).replace('+', '-')
                    server = proxy['server']
                    port = str(proxy['port'])
                    password = format.base64_encode(proxy['password'])
                    cipher = proxy['cipher']
                    protocol = proxy['protocol']
                    obfs = proxy['obfs']
                    param_dic = {'group': 'U1NSUHJvdmlkZXI', 'obfsparam':'', 'protoparam':''}
                    for key in param_dic.keys():
                        try:
                            param_dic.update({key: format.base64_encode(proxy[key])})
                        except Exception:
                            pass
                    group, obfsparam, protoparam = param_dic['group'], param_dic['obfsparam'], param_dic['protoparam']
                    ssr_proxy = 'ssr://'+format.base64_encode(server+':'+port+':'+protocol+':'+cipher+':'+obfs+':'+password+'/?group='+group+'&remarks='+remarks+'&obfsparam='+obfsparam+'&protoparam='+protoparam+'\n')
                    url_list.append(ssr_proxy)
            except Exception:
                pass

        url_content = ''.join(url_list)
        return url_content
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
    def base64_encode(content): # 将 URL 内容转换为 Base64
        if content == None:
            content = ''
        base64_content = base64.b64encode(content.encode('utf-8')).decode('ascii')
        return base64_content

def config_output(subscription,target='clash',config={'duplicate_remove': False, 'format_remarks': ''}):
    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('./subconverter')

    temp = format(subscription,config).output
    if target == 'url':
        output = format.base64_decode(temp)
    elif target == 'base64':
        output = temp
    else:
        with open(f'./temp', 'w', encoding= 'utf-8') as temp_file:
            temp_file.write(temp)
            if os.name == 'posix':
                os.system(f'./subconverter -g --artifact \"{target}\"')
            elif os.name == 'nt':
                os.system(f'subconverter.exe -g --artifact \"{target}\"')
        with open(f'./temp', 'r', encoding= 'utf-8') as temp_file:
            output = temp_file.read()

        os.remove('./temp')
    os.chdir(work_dir)

    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert between various proxy subscription formats using Subconverter.')
    parser.add_argument('--subscription', '-s', help='Your subscription url or local file path.', required=True)
    parser.add_argument('--target', '-t', help='Target convert format, support base64, clash, clash_provider, quanx.', default='clash')
    parser.add_argument('--output', '-o', help='Target path to output, default value is the Subconverter root directionary.', default='./')
    args = parser.parse_args()

    subscription = args.subscription
    target = args.target
    output_dir = args.output
    
    content = format(subscription).output
    
    work_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('./subconverter')

    with open(f'./temp', 'w+', encoding= 'utf-8') as temp_file:
        temp_file.write(content)
        if os.name == 'posix':
            os.system(f'./subconverter -g --artifact \"{target}\"')
        elif os.name == 'nt':
            os.system(f'subconverter.exe -g --artifact \"{target}\"')
    with open(f'./temp', 'r', encoding= 'utf-8') as temp_file:
        temp = ''
        while True:
            content = temp_file.read(100)
            if not content:
                break
            temp += content
    with open(output_dir, 'w', encoding= 'utf-8') as temp_file:
        temp_file.write(temp)
    os.remove('./temp')
    os.chdir(work_dir)