#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 15:15
# @Author  : Evan.hu

import os
import settings,traceback
from DataServer.AnyRobotDatePre.DataGeneration import dataServer
from entity.opertation_file import getServer, getTestCaseInfo
from libs.error import runException


def isRunPara(server,model):

    if len(settings.date) == 0:
        TestCase = getServer(True)
    else:
        TestCase = settings.date

    serverAR = TestCase.keys()

    # 首先判断是否全量运行测试用例
    if server=='anyrobot' and model == 'all':
        serverName,modelName = '',''
        return serverName,modelName

    # 判断测试用例运行server
    if server in serverAR:
        # 判断模块是否对应
        if model in TestCase[server].keys():
            return server,model
        else:
            return 1
    else:
        return 0

def createFile():
    result_path = settings.REPORT_RESULT
    report_path = settings.REPORT_URL
    log_path = settings.LOG_PATH
    path = [report_path, result_path, log_path]
    for key in path:
        if not os.path.exists(key):
            os.makedirs(key)

def initEnv():
    # 初始化系统文件
    result_path = settings.REPORT_RESULT
    report_path = settings.REPORT_URL
    log_path = settings.LOG_PATH
    path = [report_path, result_path, log_path]
    for key in path:
        if not os.path.exists(key):
            os.makedirs(key)

    # 数据初始化
    try:
        dataServer().dataServerGen()
    except Exception as e:
        msg = traceback.format_exc()
        try:
            raise runException("初始化数据失败: {msg}".format(msg=msg))
        except runException as e_result:
            msg = e_result
            return msg

    # 加载测试用例集合到内存中
    try:
        date = getServer(True)
        settings.date = date
    except Exception as e:
        msg = traceback.format_exc()
        try:
            raise runException("测试用例加载失败:{msg}".format(msg=msg))
        except runException as e_result:
            msg = e_result
            return msg
    return 0

if __name__ == '__main__':
    date = isRunPara('anyrobot','all')
    print(date)
    # initEnv()