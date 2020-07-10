#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 15:52
# @Author  : Evan.hu

import json,os
import time

from CaseServices.AIScript.comm.AItool import read,get_parameter,isdir,create_init,write

INTERFACE_PATH = r'C:\UT_AR_TestFramework\interface'
TEST_CASE_PATH = r'C:\UT_AR_TestFramework\TestCases'
TEST_DATE_PATH = r'C:\UT_AR_TestFramework\data'
TEMPLATES_PATH = r'C:\UT_AR_TestFramework\CaseServices\AIScript\template'


def caseGen(info):
    # 判断模块是否存在,不存在就创建
    server = info['server']
    model = info['model']
    path = TEST_CASE_PATH + os.path.sep + server + os.path.sep + model
    isdir(path)

    # 判断server和model是否存在__init__.py文件
    serverPath = TEST_CASE_PATH + os.path.sep + server
    create_init(path)
    create_init(serverPath)

    # 获取测试用例模板
    text = read(TEMPLATES_PATH, 'interfaceCase.txt')

    # 参数化替换
    timeInfo = time.localtime()
    result = u"%s/%s/%s %s:%s" % (timeInfo.tm_year, timeInfo.tm_mon, timeInfo.tm_mday, timeInfo.tm_hour, timeInfo.tm_min)
    pare = {
        'server': info['server'],
        'model': info['model'],
        'interface_name': info['interface_name'],
        'interface_method_1': info['interface_name'] + '_' + info['method'],
        'interface_method_2': info['interface_name'] + '_' + info['method'],
        'class': info['model'],
        'method': 'test' + '_' + info['interface_name'] + '_' + info['method'],
        'time' : result
    }
    text = get_parameter(text, pare)
    # print(text)

    # 生成测试用例case,如果存在则跳过脚本
    path = TEST_CASE_PATH + os.path.sep + server + os.path.sep + model
    name = 'test' + '_' + info['interface_name']
    # file_name = path + os.path.sep + name + '.py'
    # if not search_file(file_name):
    #     write(text, path, name)
    write(text, path, name)