#!/usr/bin/env python3

import os, urllib
import configparser, json

from sub_merge import merge
from sub_update import update


config_file = './utils/config.ini'
external_config = {'speedtest': './utils/litespeedtest/config.json', 'subconverter': './utils/subconverter/generate.ini'}


def configparse(section):
    config = configparser.ConfigParser()
    config.read(config_file)
    if section == 'common':
        return config['common']
    elif section == 'subconverter':
        return config['subconverter']
    elif section == 'speedtest':
        return config['speedtest']

def externalconfighandler():
    config = configparser.ConfigParser()
    config.read(config_file)
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
    

if __name__ == '__main__':
    externalconfighandler() # Initialize config

    print('Downloading Country.mmdb...')
    try:
        urllib.request.urlretrieve('https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb', './utils/Country.mmdb')
        print('Success!\n')
    except Exception:
        print('Failed!\n')
        pass


    if configparse('common').getboolean('update_enabled'):
        config = configparse('common')
        update(config)

    if configparse('common').getboolean('merge_enabled') :
        file_dir = configparse('common')
        format_config = configparse('subconverter')
        merge(file_dir, format_config)

    if configparse('common').getboolean('speedtest_enabled'):
        share_file = configparse('common')['share_file']
        share_file_clash = configparse('common')['share_file_clash']
        range = configparse('speedtest')['output_range']
        os.system(f'proxychains python3 ./utils/litespeedtest/output.py --target \"../../{share_file}\" --range \"{range}\"')
        os.system(f'python3 ./utils/sub_convert.py --subscription \"{share_file}\" --target \"clash\" --output \"../../{share_file_clash}\"')