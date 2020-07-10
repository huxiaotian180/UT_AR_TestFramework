#!/usr/bin/env python33
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:29
# @Author  : Evan.hu
from entity.operation_json import OperetionJson
from entity.mysql_pool import select
import traceback


def assertGetCount(info):
    # 获取返回报文
    date = info['response']

    Json = OperetionJson(date)
    db_test = Json.get_value(info['original_date']['verify']['getAssertCount']['key'])

    count = db_test[0]
    sql = 'select id from {table};'.format(table=info['original_date']['verify']['getAssertCount']['db'])
    try:
        date = select(sql)
    except Exception as e:
        msg = {
            'isSkip': '数据库查询{sql},\n数据库查询报错信息{msg}'.format(sql=sql, msg=traceback.format_exc())
        }
        return msg

    if db_test:
        if count == len(date):
            msg = {
                'flag': True
            }
        else:
            msg = {
                'flag': False,
                'msg': {
                    'except': '接口返回结果 : 接口返回{count1}记录'.format(count1=count),
                    'actual': '数据库查询结果 : 数据库查询{count2}记录'.format(count2=len(date)),
                    'actualMsg': '数据库查询信息 : 数据库查询{msg2}记录'.format(msg2=date),
                }
            }

        return msg

    else:
        msg = {
            'flag': False,
            'msg': {
                'except': '接口返回结果 : 接口返回报文不存在{key}'.format(key=info['original_date']['verify']['getAssertCount']['field']),
                'actual': '数据库查询结果 : 数据库查询{count2}记录'.format(count2=len(date)),
                'actualMsg': '数据库查询信息 : 数据库查询{msg2}记录'.format(msg2=date),
            }
        }

        return msg

def assertGetAll(info):
    # 获取返回报文
    date = info['response']
    Json = OperetionJson(date)
    db_test = Json.get_value(info['original_date']['verify']['getAssertAll']['key'])
    sql = 'select id from {table} where id="{id}";'.format(table=info['original_date']['verify']['getAssertAll']['db'],id=info['original_date']['verify']['getAssertAll']['key'])
    try:
        data = select(sql)
    except Exception as e:
        msg = {
            'isSkip': '数据库查询{sql},\n数据库查询报错信息{msg}'.format(sql=sql, msg=traceback.format_exc())
        }
        return msg

    if db_test:
        id = []
        for date in data:
            id.append(date[0])
        if len(db_test) == len(id):
            msg = {
                'flag': True,
                'msg': ''
            }
            return msg
        else:
            msg = {
                'flag': False,
                'msg': '接口实际返回{count1}记录与数据库查询{count2}记录不一致'.format(count1=len(db_test),count2=len(id))
            }
            return msg

    else:
        count1 = 0
        count2 = select(sql)
        if count1 != len(count2):
            msg = {
                'flag': False,
                'msg': '接口实际返回{count1}记录与数据库查询{count2}记录不一致'.format(count1=count1, count2=len(count2))
            }
            return msg


        msg = {
                'flag': True
            }
        return msg


def assertGetId(info):
    # 获取返回报文
    date = info['response']
    Json = OperetionJson(date)
    key = info['original_date']['verify']['getAssertId']['key']
    db_test = Json.get_value(key)
    sql = "select id from {table} where id='{id}';".format(table=info['original_date']['verify']['getAssertId']['db'], id=info['original_date']['verify']['getAssertId']['id'])
    try:
        data = select(sql)
    except Exception as e:
        msg = {
            'isSkip': '数据库查询{sql},\n数据库查询报错信息{msg}'.format(sql=sql, msg=traceback.format_exc())
        }
        return msg

    if db_test:
        if len(data) == 1:
            if db_test[0] == data[0][0]:
                msg = {
                    'flag': True,
                    'msg': ''
                }
                return msg

            else:
                msg = {
                    'flag': False,
                    'msg': {
                    'except': '接口返回结果 : 接口返回{id1}记录'.format(id1=db_test[0]),
                    'actual': '数据库查询结果 : 数据库查询{id2}记录'.format(id2=data[0][0])
                    }
                }
                return msg

        elif len(data) == 0:
            msg = {
                'flag': False,
                'msg': {
                    'except': '接口返回结果 : 接口返回{id1}记录'.format(id1=db_test[0]),
                    'actual': '数据库查询结果 : 数据库查询为空'
                }
            }
            return msg

        else:
            msg = {
                'flag': False,
                'msg': {
                    'except': '接口返回结果 : 接口返回{id1}记录'.format(id1=db_test[0]),
                    'actual': '数据库查询结果 : 数据库查询{id2}记录'.format(id2=data[0][0])
                }
            }
            return msg

    else:
        if len(data) > 0:
            msg = {
                'flag': False,
                'msg': {
                    'except': '接口返回结果 : 接口返回数据为空',
                    'actual': '数据库查询结果 : 数据库查询{id2}记录'.format(id2=data[0][0])
                }
            }
            return msg

        else:
            msg = {
                'flag': True,
                'msg': ''
            }
            return msg
