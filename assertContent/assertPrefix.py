#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 11:38
# @Author  : Evan.hu
from entity.operation_json import OperetionJson
import pdb

# 判断返回内容是否可以转化成字典和列表
def dateDict(date):
    data1 = str(date).replace('true', 'True')
    data2 = str(data1).replace('false', 'False')
    try:
        eval(data2)
        return True
    except Exception as e:
        return False


def assertPrefix(info):
    date = info['response']
    statusCode = [100,200,202,301,302]
    if info['code'] not in statusCode:
        msg = {
            'actual': {
                'flag': True,
                'msg': '实际结果 : \n接口返回状态码{code}\n接口实际返回body : {body}'.format(code=info['code'], body=date)
            }
        }
        return msg

    elif isinstance(date,dict):
        Json = OperetionJson(date)
        db_test = Json.get_value('message')  # 没找到是false
        if db_test:
            if 'error' in str(db_test[0]):
                msg = {
                    'actual': {
                        'flag': True,
                        'msg': '实际结果 : \n接口返回状态码{code}\n接口实际返回body : {body}'.format(code=info['code'],body=date)
                    }
                }
            else:
                msg = {
                    'actual': {
                        'flag': False
                    }
                }
        else:
            msg = {
                'actual': {
                    'flag': False
                }
            }
        return msg

    elif isinstance(date,list):

        msg = {
                'actual': {
                    'flag': False
                }
            }

        return msg

    else:
        if 'error' in str(date):
            msg = {
                'actual': {
                    'flag': True,
                    'msg': '实际结果 : \n接口返回状态码{code}\n接口实际返回body : {body}'.format(code=info['code'],body=date)
                }
            }
            return msg

        elif 'html' in str(date):
            msg = {
                'actual': {
                    'flag': True,
                    'msg': '实际结果 : \n接口返回状态码{code}\n接口实际返回body : {body}'.format(code=info['code'],body=date)
                }
            }
            return msg

        else:
            msg = {
                'actual': {
                    'flag': False
                }
            }
            return msg
