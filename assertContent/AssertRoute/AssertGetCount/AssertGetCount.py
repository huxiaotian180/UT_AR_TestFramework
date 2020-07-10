#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 13:14
# @Author  : Evan.hu

class InfoCount(object):
    def __init__(self,key,db):
        self.key = key
        self.db = db

    def GetCount(self):
        date = {
            'AssertType':[5,],
            'getAssertCount': {
                'key': self.key,
                'db': self.db
            }
        }

        return date


if __name__ == '__main__':
    date = InfoCount(12,11).GetCount()
    print(date)