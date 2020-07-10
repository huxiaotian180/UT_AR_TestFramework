#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 9:36
# @Author  : Evan.hu
from DataServer.RepeatScene.RepeatSceneRule import RpRoute


def isRep(path,info,interface):
    if info['original_date'].get('isOperationDb') is not None:
        date = str(info['original_date']['isOperationDb']).replace(' ', '')
        if len(date) > 0:
            flag = True
        else:
            flag = False
        if flag:
            key = info['original_date']['isOperationDb']
            info = RpRoute(interface, key, info)

    info['TestCaseName'] = path[-1]
    return info