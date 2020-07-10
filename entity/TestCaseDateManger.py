#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 15:53
# @Author  : Evan.hu

import re,settings
import pytest
from entity.Frame import Framework
from entity.opertation_file import search_file
import os ,collections,copy,traceback

def TestCasePre(path):
    # 读取测试用名称
    CASE_NAME = path[-1].split(".")[0]

    # 读取测试用例模块
    # pattern = r'\\|\|/'
    # str1 = re.split(pattern, path[0])
    str1 = path[0].split(os.sep)
    CASE_MODEL = str1[-1]
    CASE_SERVER = str1[-2]

    # 根据当前文件路径找到测试数据路径
    file_path = os.path.realpath(__file__)
    TEST_CASE_DATE = os.path.dirname(os.path.dirname(file_path)) + os.path.sep + 'data'

    # 测试用例全路径
    CASE_PATH = TEST_CASE_DATE + os.path.sep + CASE_SERVER + os.path.sep + CASE_MODEL + os.path.sep + CASE_NAME + '.yaml'
    flag = not search_file(CASE_PATH)

    case_info = Framework(flag, CASE_SERVER, CASE_MODEL, CASE_NAME).skip()
    case_info['isFileExist'] = flag

    return case_info

def isSkip(case_info):

    # 判断测试用例是否跳过,判断测试用例是否存在
    if case_info['isFileExist'] == True:
        pytestmark = pytest.mark.skipif(condition=(case_info['isFileExist']),
                                        reason='测试用例不存在')
        return pytestmark
    if case_info.get('readExcept') is not None:
        pytestmark = pytest.mark.skipif(condition=(case_info['readExcept']),
                                        reason='测试用例读取异常')
        return pytestmark

    if settings.runFlag == 'off':
        pytestmark = pytest.mark.skipif(condition=(not case_info['switch']),
                                        reason='测试用例开关未开启')
    else:
        pytestmark = pytest.mark.skipif(condition=False,
                                        reason='测试用例执行')

    return pytestmark

def dataManger(case_info,parameter,interfaceName,log):
    info = {}

    # 获取请求body中参数化的数据
    info['reqPareBody'] = case_info['reqPareBody']

    # 全局开测试开关
    if case_info.get('flag') is not None:
        info['flag'] = case_info['flag']
    else:
        info['flag'] = True

    # 全局数据存储空间
    d = collections.deque()
    info['storage'] = d

    # 加入log
    info['log'] = log

    # 测试用例信息
    info['TestCaseServer'] = case_info['server']
    info['TestCaseModel'] = case_info['model']
    
    # 判断是否存在事务关联参数
    if case_info.get('transaction') is not None:
        info['transaction'] = case_info['transaction']

    try:
        # case原始数据
        originalDate = copy.deepcopy(parameter)
        originalDate.pop('req_body')
        info['original_date'] = originalDate

        # 接口请求路径,判断接口请求是否参数化,如果参数化为空则表示参数化从body读取
        if parameter.get('url_path') is not None:
            if len(parameter['url_path'].strip()) > 0:
                info['urlParameter'] = info['original_date']['url_path']
            else:
                info['urlParameter'] = case_info['urlParameter']
        else:
            info['urlParameter'] = case_info['urlParameter']

        # 接口参数
        info['request_data'] = parameter['req_body']

        # 接口请求方法
        info['method'] = case_info['method']
        info['Requests'] = case_info['Requests']

        # 测试用例开关
        if settings.runFlag == 'on':
            flag_case = True
        elif settings.runFlag =='off':
            flag_case = info['original_date']['runflag']
        else:
            flag_case = info['original_date']['runflag']

        # 测试用例全局开关判断
        if (not flag_case) or (not info['flag']):
            info['flag'] = False
            if case_info.get('skipMeg') is not None:
                info['skipMeg'] = case_info['skipMeg']

            elif not info['original_date']['runflag']:
                info['skipMeg'] = '测试用例开关未开启'
            else:
                pass
        else:
            # 调用接口步骤函数
            info = interfaceName(info)

    except Exception as e:
        info['log'].info(traceback.format_exc())
        info['flag'] = False
        info['skipMeg'] = '读取测试用例参数错误'

    return info