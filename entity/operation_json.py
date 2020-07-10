#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/2/28 16:15
#  @Author  : Evan.hu
#  @File    : operation_json

import json, settings, os
import jsonpath


class OperetionJson(object):
    def __init__(self, text):
        self.text = text

    # 根据传入字段获取json的值
    def get_value(self, name):
        # 当不存在name这个key时，返回false
        data = jsonpath.jsonpath(self.text, '$..{name}'.format(name=name))
        return data

    def search_file(self, file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False


if __name__ == '__main__':
    date = [{'ip': '10.194.143.33', 'id': 1, 'label': 'anyrobot353_645'}, {'ip': '', 'id': 2, 'label': 'anyrobot390_265'}, {'ip': 'abc.31.71.87', 'id': 3, 'label': 'anyrobot382_410'}, {'ip': '10.59.213.233', 'id': 4, 'label': ''}, {'ip': 'abc.85.19.18', 'id': 5, 'label': 'anyrobot570_113'}, {'ip': 'abc.50.90.78', 'id': 6, 'label': 'anyrobot868_16'}, {'ip':{
        'name':  'abc.86.60.35',
        'value': 12
    }, 'id': 7, 'label': 'anyrobot112_248'}, {'ip': 'abc.24.13.93', 'id': 8, 'label': 'anyrobot742_633'}]

    data1 = [1, 2, 3, 4, 5]
    a = OperetionJson(date)
    value = a.get_value('ip')
    print(value)
