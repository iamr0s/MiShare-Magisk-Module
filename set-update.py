#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        raise Exception('sys.argv')
    download_url = sys.argv[1]
    version_code = int(sys.argv[2])
    version_name = sys.argv[3]
    print(json.dumps({
        'version': version_name,
        'versionCode': version_code,
        'zipUrl': download_url,
        'changelog': 'https://raw.githubusercontent.com/iamr0s/MiShare-Magisk-Module/main/module/changelog.md'
    }, indent=2))
