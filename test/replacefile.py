#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re
import os
import sys


# 定义获取version.json中的版本方法
def get_version(jsonfile):
    config_data = open(jsonfile)
    config = json.load(config_data)
    config_data.close()
    return config['version']


# 定义替换ExportOptions.plist方法
def replace(file, value):
    with open(file, 'r') as content, open("%s.bak" % file, 'w') as content2:
        for line in content:
            content2.write(re.sub(r'/.{3,4}/v\d.{4,7}/', value, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)


if __name__ == "__main__":
    json_path = sys.argv[2] + '/src/version.json'  # 配置version.json的文件位置
    env = sys.argv[1]  # 配置环境(test,pre,prd)
    if sys.argv[1] == 'test':
        ExportOptions = '/Users/jenkins/workspace/dist/yq/testExportOptions.plist'  # 配置ExportOptions.plist文件位置
        replace(ExportOptions, '/%s/%s/' % (env, get_version(json_path)))
    elif sys.argv[1] == 'pre':
        ExportOptions = '/Users/jenkins/workspace/dist/yq/preExportOptions.plist'  # 配置ExportOptions.plist文件位置
        replace(ExportOptions, '/%s/%s/' % (env, get_version(json_path)))
    elif sys.argv[1] == 'prd':
        ExportOptions = '/Users/jenkins/workspace/dist/yq/prdExportOptions.plist'  # 配置ExportOptions.plist文件位置
        replace(ExportOptions, '/%s/%s/' % (env, get_version(json_path)))
