#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 13:21
# @Author  : Evan.hu

class InfoAll(object):
    def __init__(self,key,db):
        self.key = key
        self.db = db

    def GetAll(self):
        date = {
            'AssertType': [7, ],
            'getAssertAll': {
                'key': self.key,
                'db': self.db
            }
        }

        return date


if __name__ == '__main__':
    InfoAll(12,11).GetAll()