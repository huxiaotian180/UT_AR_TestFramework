#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 13:20
# @Author  : Evan.hu

# 装饰器实现简易限制函数调用频率，如10秒一次
import math
import time

def TimeDecorator(func):
    start_time = 0

    def inner(*args, **kwargs):
        nonlocal start_time
        t = time.time() - start_time
        if t >= 3:
            start_time = time.time()
            ret = func(*args, **kwargs)
            return ret
        else:
            print(f"设置时间间隔，倒计时{math.ceil(3 - t)}秒")
    return inner


@TimeDecorator
def foo():
    print("执行函数")
    return True

if __name__ == '__main__':
    a = foo()
    print(a)
