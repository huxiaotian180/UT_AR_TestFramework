#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 15:43
# @Author  : Evan.hu

# 获取备份目录
import json
import os

# 获取所有测试用例模块
from entity.operation_yaml import operation_yaml_read

# 获取server模块
def getList(path):
    directory = []
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isdir(path_file):
            directory.append(i)
    return directory

# 获取模块下所有测试用例
def getFile(path):
    TestCase = {}
    server = getList(path)
    for key in server:
        # 获取model
        TestCase[key] = {}
        pathModel = os.path.join(path,key)
        for model in os.listdir(pathModel):
            path_file = os.path.join(pathModel, model)
            if os.path.isdir(path_file):
                Case = []
                for file in os.listdir(path_file):
                    file = os.path.join(path_file, file)
                    if os.path.isfile(file):
                        fileName = file.split('.')[0].split('\\')[-1]
                        Case.append(fileName)
            TestCase[key][model] = Case
    return TestCase

# 文件处理
def readCase(path):
    data = getFile(path)
    back_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'backup'

    for server in data:
        for model in data[server]:
            # 创建model文件夹
            filePath = back_path + os.path.sep + server + os.path.sep + model
            if not os.path.exists(filePath):
                os.makedirs(filePath)

            # 读取model数据
            for file in data[server][model]:
                if file ==  'moduleInformation':
                    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'data'
                    namePath = file_path + os.path.sep + server + os.path.sep + model + os.path.sep + file + '.json'
                    namePathBp = filePath + os.path.sep + file + '.json'
                    dateJson = json.load(open(namePath,'r',encoding='utf-8'))
                    json.dump(dateJson,open(namePathBp,'w',encoding='utf-8'),ensure_ascii=False)
                else:

                    # 读取测试用例数据
                    CaseDate = operation_yaml_read(server,model, file)
                    name = filePath + os.path.sep + file + '.json'
                    date = json.dumps(CaseDate,ensure_ascii=False)
                    f = open(name, 'w',encoding='utf-8')
                    f.write(date)



if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'data'
    date = readCase(path)


