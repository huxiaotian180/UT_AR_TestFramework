#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 15:57
# @Author  : Evan.hu


# 读取文件
import os
from entity.opertation_file import search_file

def read(path, name):
    path = path + os.path.sep + name
    f = open(path, 'r', encoding='utf-8')
    return f.read()


# 写入py脚本文件
def write(info, path, name):
    path = path + os.path.sep + name + '.py'
    # 文件之前先检查文件是否存在
    if not search_file(path):
        f = open(path, 'w', encoding='utf-8')
        f.write(info)
        f.close()
    else:
        print('脚本存在')


# 生成脚本参数化，替换脚本内容
def get_parameter(info, parameter_list):
    contain = info
    for key in parameter_list.keys():
        text = '${' + key + '}$'
        value = str(contain).replace(text, str(parameter_list[key]))
        contain = value
    return contain


# 创建init文件
def create_init(path):
    # path = path + os.path.sep + model
    flag = True
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            if '__init__.py' in path_file:
                flag = False

    if flag:
        file = path + os.path.sep + '__init__.py'
        f = open(file, 'w')
        f.close()


# 判断是否存在目录，不存在就创建
def isdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("目录创建成功！")

# 判断文件是否存在，如果存在文件返回文件句柄
def FileExists(path, key):
    # path = path + os.path.sep + model
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            date = path_file.split('\\')[-1]
            if key == date.split('.')[0]:
                return key