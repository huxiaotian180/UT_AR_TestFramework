#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 13:47
# @Author  : Evan.hu

def default():
    return False

def RpRoute(interface,key,info):
    switcher = {
        'AlterAgentHost': ''  #OperaAlterHost(info,key).rule
    }
    return switcher.get(interface,default)()


if __name__ == '__main__':
    date = RpRoute('Agent','ip',info={})
    print(date)