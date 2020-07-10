#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 13:41
# @Author  : Evan.hu

import time

def Counter(func):
    num = 0
    def call_fun(*args, **kwargs):
        nonlocal num
        if num < 15:
            num += 1
            date = func(*args, **kwargs)
            date['count'] = num
            return date
        else:
            time.sleep(0.2)
    return call_fun
