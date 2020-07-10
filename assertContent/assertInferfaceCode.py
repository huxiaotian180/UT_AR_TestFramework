#!/usr/bin/env python33
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 10:41
# @Author  : Evan.hu


def assertCode(info):
    msg = {
        'except': {
            'code': info['original_date']['verify']['statusCode']['code'],
            'msg': '期望返回状态码 : {expect_code}'.format(expect_code=info['original_date']['verify']['statusCode']['code'])
        },
        'actual': {
            'code': info['code'],
            'msg':'实际返回状态码 : {actual_code}'.format(actual_code=info['code'])
        }
    }

    return msg
