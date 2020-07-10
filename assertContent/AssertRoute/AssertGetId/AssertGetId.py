#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 13:19
# @Author  : Evan.hu

class InfoId(object):
    def __init__(self,key,db,id):
        self.id = id
        self.key = key
        self.db = db

    def GetId(self):
        date = {
            'AssertType': [6, ],
            'getAssertId': {
                'id': self.id,
                'key': self.key,
                'db': self.db
            }
        }

        return date


if __name__ == '__main__':
    InfoId(12,11).GetId()