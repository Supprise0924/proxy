import os
import yaml

from yaml import SafeLoader
from urllib import request

from sub_convert import sub_convert
from sub_merge import sub_merge

def init(config_file):
    with open('file','r') as reader:
        config = yaml.load(reader, Loader=SafeLoader)
    config = {
        'subscription': {'dir': config['subscription']['dir'], 'sublist-file': config['subscription']['sublist-file']},
        'provider': {'dir': config['provider']['provider'], 'config': config['provider']['config']},
        'outfile': {'base64': config['outfile']['base64'], 'clash': config['outfile']['clash'], 'readme': config['outfile']['readme']},
        'subconvert': {'geoip-url': config['subconvert']['geoip-url'], 'dup-rm': config['subconvert']['dup-rm'], 'name-format': config['subconvert']['name-format']},
        'speedtest': {'num': config['speedtest']['num']}
    }

    #Update Country.mmdb
    print('Downloading Country.mmdb...')
    try:
        request.urlretrieve(config['subconvert']['geoip-url'], './utils/Country.mmdb')
        print('Success!\n')
    except Exception:
        print('Failed!\n')
        pass

    return config

if __name__ == '__main__':
    init('./utils/config.yaml')

