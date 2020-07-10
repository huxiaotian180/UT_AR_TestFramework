#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/2 16:30
#  @Author  : Evan.hu
#  @File    : app.py

import settings, re, os ,json
from configuration.configYaml import configManage
from entity.operationYaml import operationRead, operationWrite
from entity.operation_yaml import operation_yaml_read
from entity.operation_json import OperetionJson

def file_clear():
    # 清理历史测试报告文件
    path = settings.REPORT_RESULT
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            for f in os.listdir(path_file):
                path_file2 = os.path.join(path_file, f)
                if os.path.isfile(path_file2):
                    os.remove(path_file2)


def search_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False


def properties():
    path = settings.REPORT_RESULT + os.path.sep + 'environment.properties'
    with open(path, 'w') as f:
        ip = configManage().getIp
        port = configManage().getPort
        f.write("environment={ip}\n".format(ip=ip))
        f.write("port={port}".format(port=port))


def alter_env(new_ip, new_port):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'configuration'
    name = 'config.yaml'
    date = operationRead(path, name)

    # 替换ip参数

    date['TestEnv']['ip'] = new_ip
    date['TestEnv']['port'] = new_port

    # 写入换参数
    operationWrite(path,name,date)

    # 查看现在系统IP和PORT
    env = {}
    date_current = operationRead(path, name)
    env['current_ip'] = date_current['TestEnv']['ip']
    env['current_port'] = date_current['TestEnv']['port']
    print(env)
    return env


def get_parameter(info, parameter_list):
    # 删除影响json转化格式字段
    impactList = ['storage', 'log']
    impactDict = {}
    for deleteKey in impactList:
        if info.get(deleteKey) is not None:
            impactDict[deleteKey] = info[deleteKey]
            info.pop(deleteKey)

    # 参数化数据获取
    for key in parameter_list.keys():
        jn = OperetionJson(info)
        date = jn.get_value(key)
        if date:
            keyValue = '${' + key + '}$'
            if keyValue == date[0]:
                value = str(info).replace(str(date[0]), parameter_list[key])
                info = eval(value)
            else:
                strValue = str(date[0]).replace(keyValue, parameter_list[key])
                value = str(info).replace(str(date[0]), strValue)
                info = eval(value)

        elif key in str(info):
            text = '${' + key + '}$'
            value = str(info).replace(text, str(parameter_list[key]))
            info = eval(value)

    for getKey in impactDict.keys():
        info[getKey] = impactDict[getKey]

    return info

def getServer(flag):
    # 获取系统全部server用例
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'data'
    directory = []
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isdir(path_file):
            directory.append(i)

    # 获取具体server下面的测试用例模块
    TestCase = {}
    server = directory
    for key in server:
        # 获取model
        TestCase[key] = {}
        pathModel = os.path.join(path, key)
        for model in os.listdir(pathModel):
            path_file = os.path.join(pathModel, model)
            if os.path.isdir(path_file):
                Case = []
                for file in os.listdir(path_file):
                    file = os.path.join(path_file, file)
                    if os.path.isfile(file):
                        # pattern = r'\\|\|/'
                        # fileName = re.split(pattern,file)[-1].split('.')[0]
                        fileName = file.split('.')[0].split(os.sep)[-1]
                        if flag == True:
                            if fileName == 'moduleInformation':
                                continue
                        Case.append(fileName)
            TestCase[key][model] = Case
    return TestCase


def getTestCaseInfo():
    info = {}
    date = getServer(False)
    countAll = 0
    for server in date.keys():
        info[server] = {}
        for model in date[server].keys():
            count = 0
            info[server][model] = {}
            for file in date[server][model]:
                if file == 'moduleInformation':
                    # 获取测试用例负责人信息
                    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'data'
                    namePath = file_path + os.path.sep + server + os.path.sep + model + os.path.sep + file + '.json'
                    moduleInfo = json.load(open(namePath,'r',encoding='utf-8'))
                    auth = moduleInfo['responsible']
                else:
                    value = operation_yaml_read(server, model, file)
                    try:
                        countCase = len(value['testcases'].keys())
                    except Exception as e:
                        print(server)
                        print(model)
                        print(file)
                        exit(0)

                    count = count + countCase
                    countAll += countCase
            info[server][model]['count'] = count
            info[server][model]['auth'] = auth

    info['all'] = countAll
    return info

if __name__ == '__main__':
    date = getTestCaseInfo()
    settings.date = date
    print(settings.date)