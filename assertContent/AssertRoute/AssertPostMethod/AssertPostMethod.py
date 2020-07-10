#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 11:13
# @Author  : Evan.hu

class PostRule(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def GetPostRule(self):
        # path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        # name = 'assertType.yaml'
        # date = operationRead(path, name)
        # date['responseField']['Verify_field'] = self.key
        # date['responseField']['expect'] = self.value

        # 原始断言组合
        verify = {
            'AssertType': [2, ],
            'responseField': {
                'Verify_field': self.key,
                'expect': self.value
            }
        }

        return verify