#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 15:53
# @Author  : Evan.hu
import json,traceback
import os

from CaseServices.AIScript.AIrequestBody import bodyGen
from entity.operation_yaml import operation_yaml_write, operation_yaml_read
from CaseServices.AIScript.comm.AItool import isdir,FileExists

INTERFACE_PATH = r'C:\UT_AR_TestFramework\interface'
TEST_CASE_PATH = r'C:\UT_AR_TestFramework\TestCases'
TEST_DATE_PATH = r'C:\UT_AR_TestFramework\data'
TEMPLATES_PATH = r'C:\UT_AR_TestFramework\CaseServices\AIScript\template'
BODY_PATH = r'C:\UT_AR_TestFramework\requestBody'


def caseDateGen(info):
    # 获取写入yaml文件模块和文件名称
    case_name = 'test' + '_' + info['interface_name']

    # 判断模块是否存在,不存在就创建
    server = info['server']
    model = info['model']
    path = TEST_DATE_PATH + os.path.sep + server + os.path.sep + model
    isdir(path)

    # 接口断言
    assertText = {
        'AssertType': 0
    }

    flag_type = info.get('type')
    if flag_type:
        if len(str(info['type'])) > 0 and flag_type :
            assertText['type'] = int(info['type'])

    flag_id = info.get('id')
    if flag_id:
        if len(str(info['id'])) >0 and flag_id:
            assertText['id'] = info['id']

    flag_key = info.get('key')
    if flag_key:
        if len(str(info['key'])) > 0 and flag_key:
            assertText['key'] = info['key']

    flag_value = info.get('value')
    if flag_value is not None:
        if len(str(info['value'])) > 0 and flag_value:
            if isinstance(info['value'],float):
                value = int(info['value'])
            else:
                value = info['value']
            assertText['value'] = value

    flag_db = info.get('db')
    if flag_db:
        if len(str(info['db'])) > 0 and flag_db :
            assertText['db'] = info['db']

    # 判断是否存在测试案例，如果存在找到测试用例，追加测试场景
    result = FileExists(path, case_name)
    if result is None:
        # 接口请求body转化
        body = info['body']
        if len(body) > 0:
            print('存在请求body')
            try:
                body_dict = eval(body)
            except Exception as e:
                body_dict = json.loads(body)
        else:
            body_dict = ''
            # bodyflag = False
            print('请求中不存在body')
    else:
        body_dict = ''

    TestDate = {}
    Case = info['TestCase']
    TestDate[Case] = {}
    TestDate[Case]['Description'] = info['Description']
    TestDate[Case]['url_path'] = ''

    # 判断是否存在重复场景字段
    flag = info.get('OperationDb')
    if flag is not None:
        if len(info['OperationDb']) > 0:
            TestDate[Case]['isOperationDb'] = info['OperationDb']
        else:
            # TestDate[Case]['isOperationDb'] = ''
            pass
    else:
        # TestDate[Case]['isOperationDb'] = ''
        pass

    # 判断是否存在bodyPara
    flag_bodyPara = info.get('bodyPara')
    if flag_bodyPara:
        if len(info['bodyPara']) > 0 and flag_bodyPara:
            TestDate[Case]['req_body'] = {}
            id,value = str(info['bodyPara']).replace(' ','').split('=')
            TestDate[Case]['req_body'][id] = value
        else:
            TestDate[Case]['req_body'] = ''
    else:
        TestDate[Case]['req_body'] = ''

    # 测试开关
    flagRun = info.get('runflag')
    if flagRun is not None:
        TestDate[Case]['runflag'] = info['runflag']
    else:
        TestDate[Case]['runflag'] = False

    TestDate[Case]['verify'] = assertText

    Data = {
        "story_description": info['testcase_description'],
        "server":info['server'],
        "model": info['model'],
        "switch": False ,
        "request": {
            "method": info['method'],
            "url_path": ''
        },
        'body': body_dict,
        "testcases": {Case:TestDate[Case]}
    }

    # url参数化
    flag_url = info.get('url')
    flag_urlPare = info.get('urlPare')
    if flag_url is not None:
        if len(flag_url) > 0:
            Data['request']['url_path'] = info['url']

    if flag_urlPare is not None:
        if len(flag_urlPare) > 0:
            TestDate[Case]['url_path'] = info['urlPare']
        else:
            TestDate[Case].pop('url_path')
    else:
        TestDate[Case].pop('url_path')

    # 判断是否存在header
    flag = info.get('header')
    if flag is not None:
        headers = (info['header'])
        if len(headers) > 0:
            try:
                header = json.loads(headers)
                Data['request']['header'] = header
            except Exception as e:
                try:
                    header = eval(headers)
                    Data['request']['header'] = header
                except Exception as e:
                    traceback.print_exc()

    # 判断是否存在测试案例，如果存在找到测试用例，追加测试场景

    if result is None:
        # 写入测试数据yaml
        print('测试用例不存在，创建测试用例')
        operation_yaml_write(server,model, case_name, Data)
    else:
        # 测试用例存在，更新测试用例
        print('测试用例存在，更新测试用例')

        date = operation_yaml_read(server,model,result)
        date['testcases'][Case] = TestDate[Case]
        operation_yaml_write(server,model, result, date)