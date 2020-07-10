#!/usr/bin/env python33
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 9:43
# @Author  : Evan.hu

from entity.operation_json import OperetionJson
from interface.ar_manager.etl.commit.getEtlInfo import getEtlIdInfo


def getResponseKey(info):
    url = info['url']
    key = info['original_date']['verify']['responseCode']['key']
    actualDate = getEtlIdInfo(url,key)
    expectDate = info['original_date']['verify']['responseCode']['value']
    if isinstance(actualDate,dict) and isinstance(expectDate,dict):
        if actualDate == expectDate:  # bug
            msg = {
                'except': {
                    'keyValue': False,
                    'msg': '期望结果 : 接口请求报文存在非法参数,接口请求修改失败'
                },
                'actual': {
                    'keyValue': True,
                    'msg': '实际结果 : 接口请求报文存在非法参数,接口请求修改成功,{key} = {value}'.format(key=key, value=expectDate)
                }
            }
        else:
            msg = {
                'except': {
                    'keyValue': True,
                    'msg': ''
                },
                'actual': {
                    'keyValue': True,
                    'msg': ''
                }
            }

        return msg
    elif isinstance(actualDate,list) and isinstance(expectDate,list):
        diff1 = set(actualDate).difference(set(expectDate))
        diff2 = set(set(expectDate)).difference(actualDate)
        if len(diff1) == 0 and len(diff2) == 0:
            msg = {
                'except': {
                    'keyValue': False,
                    'msg': '期望结果 : 接口请求报文存在非法参数,接口请求修改失败'
                },
                'actual': {
                    'keyValue': True,
                    'msg': '实际结果 : 接口请求报文存在非法参数,接口请求修改成功,{key} = {value}'.format(key=key, value=expectDate)
                }
            }
        else:
            msg = {
                'except': {
                    'keyValue': True,
                    'msg': ''
                },
                'actual': {
                    'keyValue': True,
                    'msg': ''
                }
            }
        return msg

    else:
        if str(actualDate) == str(expectDate):  # bug
            msg = {
                'except': {
                    'keyValue': False,
                    'msg': '期望结果 : 接口请求报文存在非法参数,接口请求修改失败'
                },
                'actual': {
                    'keyValue': True,
                    'msg': '实际结果 : 接口请求报文存在非法参数,接口请求修改成功,{key} = {value}'.format(key=key, value=expectDate)
                }
            }
        else:
            msg = {
                'except': {
                    'keyValue': True,
                    'msg': ''
                },
                'actual': {
                    'keyValue': True,
                    'msg': ''
                }
            }

        return msg

def assertKey(info):
    # 判断是否存在flag参数
    if info['original_date']['verify']['responseCode'].get('flag') is not None:
        return getResponseKey(info)

    date = info['response']
    if len(date) == 0:
        msg = {
            'failed': '接口返回内容为空'
        }
        return msg

    elif not isinstance(date,list) or not isinstance(date,dict):
        try:
            data1 = str(date).replace('true', 'True')
            data2 = str(data1).replace('false', 'False')
            date = eval(data2)

        except Exception as e:
            msg = {
                'failed': '接口返回报文格式错误: 接口返回码: {code},实际返回内容: message: {msg}'.format(code=info['code'], msg=date)
            }
            return msg

    # 获取接口断言信息
    Json = OperetionJson(date)
    db_test = Json.get_value(info['original_date']['verify']['responseCode']['key'])
    expectValue = info['original_date']['verify']['responseCode']['value']

    if isinstance(expectValue,float):
        expectValue = int(expectValue)

    if db_test:
        msg = {
            'except': {
                'keyValue': expectValue,
                'msg': '期望结果 : 接口返回报文期望结果,{key} = {value}'.format(key=info['original_date']['verify']['responseCode']['key'], value=expectValue)
            },
            'actual': {
                'keyValue': db_test[0],
                'msg': '实际结果 : 接口返回报文实际返回结果,{key} = {value}'.format(key=info['original_date']['verify']['responseCode']['key'], value=db_test[0])
            }
        }

        return msg

    else:
        msg = {
            'except': {
                'keyValue': expectValue,
                'msg': '期望结果 : 接口返回报文期望结果,{key} = {value}'.format(key=info['original_date']['verify']['responseCode']['key'], value=expectValue)
            },
            'actual': {
                'keyValue': '',
                'msg': '实际结果 : 接口返回报文不存在{key} '.format(key=info['original_date']['verify']['responseCode']['key'])
            }
        }
        return msg