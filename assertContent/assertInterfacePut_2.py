#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 11:37
# @Author  : Evan.hu

from entity.mysql_pool import select
import traceback
import hashlib

def getMd5(date):
    m = hashlib.md5(str(date).encode())
    result = m.hexdigest()
    return result

def assertPut(info):
    # 接口验证信息
    isAlterFlag = info['original_date']['verify']['putAssert']['isAlter']
    expectMsg = ''
    if isAlterFlag:
        expectMsg = '期望结果 : 请求body参数合法创建或修改成功'

    else:
        if info.get('reqPareBody') is not None:
            keys = info['reqPareBody'].keys()
        else:
            keys = ''
        if len(keys) == 0:
            expectMsg = '期望结果 : 具体缺陷描参见测试用例描述'
        else:
            for key in keys:
                expectMsg = '期望结果 : 请求body存在不合法参数创建或修改资源失败 : {key}={value}'.format(key=key, value=info['reqPareBody'][key])

    # 获取接口断言相关字段
    dbTest_before = info['assertPutInfo']['dbTest_before']
    sql = info['assertPutInfo']['sql']
    try:
        date = select(sql)
        dbTest_after = date[0][0]
        md5_dbTest_before = getMd5(dbTest_before)
        md5_dbTest_after = getMd5(dbTest_after)
        msg = {
            'except': {
                'flag': isAlterFlag,
                'msg': '{expect_message}'.format(expect_message=expectMsg)
            },
            'db': {
                'msg': '数据库查询信息{db_message}'.format(db_message=dbTest_after)
            }
        }
        if md5_dbTest_before == md5_dbTest_after:  # 数据源未修改
            actual = {
                'actual': {
                    'flag': False,
                    'msg': '实际结果 : 接口请求数据源未修改'
                }
            }
            msg['actual'] = actual['actual']
        else:   # 数据源修改成功
            actual = {
                'actual': {
                    'flag': True,
                    'msg': '实际结果 : 接口请求数据源修改成功'
                }
            }
            msg['actual'] = actual['actual']

        return msg
    except Exception as e:
        msg = {
            'isSkip': '数据库查询失败 : \nsql={sql}\nmsg={msg}'.format(sql=sql, msg=traceback.format_exc())
        }
        return msg

