#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 11:25
# @Author  : Evan.hu

class StatusCode(object):
    def __init__(self,value):
        self.value = value

    def GetStatusCode(self):
        # path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        # name = 'assertType.yaml'
        # date = operationRead(path, name)
        # date['statusCode']['code'] = self.value

        # 原始断言组合
        verify = {
            'AssertType': [0,],
            'statusCode':{
                'code': self.value
            }
        }

        return verify


if __name__ == '__main__':
    date = StatusCode(12).GetStatusCode()
    print(date)
