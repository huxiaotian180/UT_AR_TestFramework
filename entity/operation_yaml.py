#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/2/28 16:22
#  @Author  : Evan.hu
#  @File    : operation_yaml

import os,traceback
from ruamel import yaml


def search_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

# 字典格式写入yaml文件
def operation_yaml_write(server,model, case_name, case_info):
    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'data'
    file_name = file_path + os.path.sep + server + os.path.sep + model + os.path.sep + case_name + '.yaml'
    with open(file_name, 'w+', encoding='utf-8') as f:
        try:
            yaml.dump(case_info, f, allow_unicode=True,Dumper=yaml.RoundTripDumper)
        except Exception as e:
            traceback.print_exc()


# 读取yaml文件
def operation_yaml_read(server,model, case_name):
    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'data'
    file_name = file_path + os.path.sep + server + os.path.sep + model + os.path.sep + case_name + '.yaml'
    if search_file(file_name):
        with open(file_name, encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                return data
            except Exception as e:
                traceback.print_exc()

if __name__ == '__main__':
    date = operation_yaml_read('dbio','serviceManager','test_DBIOAddService')
    print(date)