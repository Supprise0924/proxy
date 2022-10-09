#!/usr/bin/env python3

import os

from sub_merge import merge
from sub_update import update
from config_parser import configparse, externalhandler

if __name__ == '__main__':
    externalhandler() # Initialize config

    if configparse('common').getboolean('update_enabled'):
        config = configparse('common')
        update(config)

    if configparse('common').getboolean('merge_enabled') :
        file_dir = configparse('common')
        format_config = configparse('subconverter')
        merge(file_dir, format_config)

    if configparse('common').getboolean('speedtest_enabled'):
        os.system('python3 ./utils/litespeedtest/output.py --target \"./Eternity\" --num 99')