#!/usr/bin/env python3

import os, urllib
import configparser

from sub_update import update
from sub_merge import merge

config_file = './utils/config.ini'

def configparse(section):
    config = configparser.ConfigParser()
    config.read(config_file)
    if section == 'common':
        return config['common']
    elif section == 'subconverter':
        return config['subconverter']
    elif section == 'speedtest':
        return config['speedtest']

if __name__ == '__main__':

    try:
        print('Downloading Country.mmdb...')
        urllib.request.urlretrieve('https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb', './utils/Country.mmdb')
        print('Success!\n')
    except Exception:
        print('Failed!\n')
        pass

    if configparse('common').getboolean('update_enabled'):
        config = configparse('common')
        update(config)

    if configparse('common').getboolean('merge_enabled'):
        file_dir = configparse('common')
        format_config = configparse('subconverter')
        merge(file_dir, format_config)

    if configparse('common').getboolean('speedtest_enabled'):
        share_file = configparse('common')['share_file']
        share_file_clash = configparse('common')['share_file_clash']
        subscription = configparse('speedtest')['subscription']
        range = configparse('speedtest')['output_range']
        os.system(f'proxychains python3 ./utils/litespeedtest/speedtest.py --subscription \"../../{subscription}\" --range \"{range}\" --path \"../../{share_file}\"')
        os.system(f'python3 ./utils/subconverter/subconvert.py --subscription \"../../{share_file}\" --target \"clash\" --output \"../../{share_file_clash}\"')