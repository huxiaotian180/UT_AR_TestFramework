#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 10:17
# @Author  : Evan.hu


# 字典格式写入yaml文件
import os
import traceback
from ruamel import yaml

def search_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

def operationWrite(path, name, info):
    filePath = path + os.path.sep + name
    with open(filePath, 'w+', encoding='utf-8') as f:
        try:
            yaml.dump(info, f, allow_unicode=True,Dumper=yaml.RoundTripDumper)
        except Exception as e:
            traceback.print_exc()


# 读取yaml文件
def operationRead(path, name):
    filePath = path + os.path.sep + name
    # print(filePath)
    if search_file(filePath):
        with open(filePath, encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                return data
            except Exception as e:
                traceback.print_exc()


if __name__ == '__main__':
    filePath = r'C:\UT_AR_TestFramework\data'
    fileName = 'TestCase1.yaml'
    date = {
    "description": "",
    "filters": {
        "host": [
            {
                "negative": 0,
                "type": 0,
                "value": "192.168.84.26"
            }
        ],
        "type": [
            {
                "negative": 0,
                "type": 0,
                "value": "场景测试"
            },
            {
                "type": 2
            },
            {
                "negative": 0,
                "type": 0,
                "value": "AS访问日志"
            }
        ],
        "tags": [
            "*"
        ],
        "logWareHouse": [
            "TNMKAjz7"
        ],
        "advance": ""
    },
    "groupName": "es日志分组",
    "parentGroupId": ""
}
    date = operationRead(filePath,fileName)
    print(date)
