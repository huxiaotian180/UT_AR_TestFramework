#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 11:12
# @Author  : Evan.hu

def default():
    pass

class DeleteRule(object):
    def __init__(self,id,db):
        self.id = id
        self.db = db

    def GetDelete(self):
        verify = {
                'AssertType': [3, ],
                'deleteAssert': {
                    'id': self.id,
                    'table': self.db
                }
        }
        return verify

if __name__ == '__main__':
    date = DeleteRule('TemplateID','ip').GetDelete()
    print(date)