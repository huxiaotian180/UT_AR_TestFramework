#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 15:51
# @Author  : Evan.hu
import time,os
from CaseServices.AIScript.comm.AItool import read,get_parameter,isdir,create_init,write
from entity.opertation_file import search_file

INTERFACE_PATH = r'C:\UT_AR_TestFramework\interface'
TEMPLATES_PATH = r'C:\UT_AR_TestFramework\CaseServices\AIScript\template'


# 写入接口
def interfaceGen(info):
    # 判断模块是否存在,不存在就创建
    server = info['server']
    model = info['model']
    path = INTERFACE_PATH + os.path.sep + server + os.path.sep + model
    isdir(path)

    # 判断server和model是否存在__init__.py文件
    serverPath = INTERFACE_PATH + os.path.sep + server
    create_init(path)
    create_init(serverPath)

    # 获取模板
    text = read(TEMPLATES_PATH, 'interface.txt')

    # 判断url
    flag_url = info.get('url')
    if flag_url is not None:
        url = info['url']
    else:
        url = info['urlPare']

    # 接口文件名称和参数化替换
    timeInfo = time.localtime()
    result = u"%s/%s/%s %s:%s" % (timeInfo.tm_year, timeInfo.tm_mon, timeInfo.tm_mday, timeInfo.tm_hour, timeInfo.tm_min)
    pare = {
        'method_name': info['interface_name'] + '_' + info['method'],
        'description': info['testcase_description'],
        'url': url,
        'method': info['method'],
        'method_interface': str(info['method']).lower(),
        'interface_name': info['interface_name'],
        'time' : result
    }

    text = get_parameter(text, pare)
    # print(text)

    # 生成测试用例脚本,如果存在脚本则跳过
    path = INTERFACE_PATH + os.path.sep + server + os.path.sep + model
    file_name = path + os.path.sep + info['interface_name'] + '.py'
    if not search_file(file_name):
        write(text, path, info['interface_name'])