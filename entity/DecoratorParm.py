#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 14:58
# @Author  : Evan.hu

def decorator(count, *args, **kwargs):
    def run_count(func):
        def run(key):
            for i in range(0, count):
                func(key)
        return run
    return run_count

@decorator(2)
def add(name):
    print('我是被装饰的函数')

if __name__ == '__main__':
    add('12')