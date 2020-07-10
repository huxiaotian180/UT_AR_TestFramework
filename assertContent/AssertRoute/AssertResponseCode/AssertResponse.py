#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 11:41
# @Author  : Evan.hu

class ResponseCode(object):
    def __init__(self,key,value,flag=''):
        self.key = key
        self.value = value
        self.flag = flag

    def GetResponseCode(self):
        # path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        # name = 'assertType.yaml'
        # date = operationRead(path, name)
        # date['responseCode']['key'] = self.key
        # date['responseCode']['value'] = self.value

        # 原始断言组合
        verify = {
            'AssertType': [1, ],
            'responseCode': {
                'key': self.key,
                'value': self.value
            }
        }

        if len(str(self.flag)) > 0:
            verify['responseCode']['flag'] = self.flag

        return verify


if __name__ == '__main__':
    date = ResponseCode(12,11).GetResponseCode()
    print(date)