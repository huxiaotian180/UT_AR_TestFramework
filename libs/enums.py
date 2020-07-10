#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/6 12:12
#  @Author  : Evan.hu
#  @File    : enums

from enum import Enum
import random

class ClientTypeEnum(Enum):
    MODEL_NAME = {
        100: "",
        200: "Export",
        300: "Agent",
        400: "AgentJobAuth"
    }


class severity_level(Enum):
    LEVEL = {
        1: "BLOCKER",  # 中断缺陷
        2: "CRITICAL",  # 临界缺陷
        3: "NORMAL",  # 普通缺陷
        4: "MINOR",  # 次要缺陷
        5: "TRIVIAL"  # 轻微缺陷
    }


class TestCase_Type(Enum):
    WORDS = ("python", "jumble", "easy", "difficult", "answer")

    Type = {
        1: {
            'value': '',
            'msg': '参数为空'
        },
        2: {
            'value': random.randint(0,100),
            'msg': '参数类型为int'
        },
        3: {
            'value': random.choice(WORDS),
            'msg': '参数类型为字符串'
        },
        4: {
            'value': [random.randint(0,100),random.randint(0,100)],
            'msg': '参数类型为list元素为int'
        },
        5: {
            'value': [random.choice(WORDS), random.randint(0, 100)],
            'msg': '参数类型为list元素为字符串'
        }
    }


class Assert_Type(Enum):
    WORDS = ("python", "jumble", "easy", "difficult", "answer")

    Type = {
        0: {
            'code': 'code',
            'msg': ''
        },
        1: {
            'key': 'code',
            'value': 'value',
            'msg': ''
        },
        2: {
            'Verify_field': 'Verify_field',
            'expect': 'expect',
            'msg': ''
        },
        3: {
            'id': 'id',
            'table': 'table',
            'msg': ''
        },
        4: {
            'table': '',
            'id':'',
            'alterText':'',
            'assertDb':'',
            'isAlter':'',
            'msg': ''
        }
    }

if __name__ == '__main__':
    a = TestCase_Type.Type.value
    print(a.keys())
    print(a[5]['value'])