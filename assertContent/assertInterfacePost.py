#!/usr/bin/env python33
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:10
# @Author  : Evan.hu

import json
from entity.operation_json import OperetionJson

def assertPost(info):
    # 获取返回报文
    date = info['response']

    # 接口验证信息
    expect = info['original_date']['verify']['responseField']['expect']
    expectMsg = ''
    if expect == True:
        expectMsg = '期望结果 : 接口创建或修改资源成功'

    else:
        if info.get('reqPareBody') is not None:
            keys = info['reqPareBody'].keys()
        else:
            keys = ''

        if len(keys) == 0:
            expectMsg = '期望结果 : 具体缺陷描参见测试用例描述'
        else:
            for key in keys:
                expectMsg = '期望结果 : 请求body存在不合法参数 : {key}={value}'.format(key=key,value=info['reqPareBody'][key])

    # 报文格式处理和转化
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
    db_test = Json.get_value(info['original_date']['verify']['responseField']['Verify_field'])  # 没找到是false

    if db_test:
        actual = True
        actualMsg = '实际结果 : 接口创建资源成功,{key} = {value}'.format(key=info['original_date']['verify']['responseField']['Verify_field'], value=db_test[0])

        msg = {
            'except': {
                'flag': expect,
                'msg': expectMsg
            },
            'actual': {
                'flag': actual,
                'msg': actualMsg
            }
        }
    else:
        actual = False
        actualMsg = '实际结果 : 接口创建资源失败,接口返回信息:{msg}'.format(msg=date)
        msg = {
            'except': {
                'flag': expect,
                'msg': expectMsg
            },
            'actual': {
                'flag': actual,
                'msg': actualMsg
            }
        }
    return msg