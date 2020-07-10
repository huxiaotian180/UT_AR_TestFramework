#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 10:38
# @Author  : Evan.hu

def default():
    pass

class PutRule(object):
    def __init__(self,id,key,value,db):
        self.key = key
        self.id = id
        self.value = value
        self.db = db

    def GetPut(self):
        table, filed = self.db.split(',')
        verify = {
            'AssertType': [4, ],
            'putAssert': {
                'id': self.id,
                'alterText': self.key,
                'table': table,
                'assertDb': filed,
                'isAlter': self.value
            }
        }

        return verify