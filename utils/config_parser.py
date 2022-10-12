#!/usr/bin/env python3

import configparser, json

config_file = './utils/config.ini'
external_config = {'speedtest': './utils/litespeedtest/config.json', 'subconverter': './utils/subconverter/generate.ini'}

config = configparser.ConfigParser()
config.read(config_file)

def configparse(section):
    if section == 'common':
        return config['common']
    elif section == 'subconverter':
        return config['subconverter']
    elif section == 'speedtest':
        return config['speedtest']

def externalhandler():
    # Litespeedtest config handler
    with open(external_config['speedtest'], 'r', encoding='utf-8') as f:
        lite_config = json.load(f)
        for key in config['speedtest']:
            if isinstance(lite_config[key],int):
                lite_config[key] = config['speedtest'].getint(key)
            else:
                lite_config[key] = config['speedtest'].get(key)
    with open(external_config['speedtest'], 'w', encoding='utf-8') as f:
        f.write(json.dumps(lite_config, sort_keys=False, indent=4, ensure_ascii=False))

    # Subconverter config handler
    # https://github.com/tindy2013/subconverter/blob/master/README-cn.md#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6
    