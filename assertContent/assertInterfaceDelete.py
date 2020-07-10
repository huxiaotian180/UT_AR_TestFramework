#!/usr/bin/env python33
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:00
# @Author  : Evan.hu
import traceback

from entity.mysql_pool import select


def assertDelete(info):
    # 获取信息表
    table = info['original_date']['verify']['deleteAssert']['table']
    id = info['original_date']['verify']['deleteAssert']['id']

    sql = "select id from {table} where id ='{id}';".format(table=table, id=id)

    try:
        date = select(sql)
    except Exception as e:
        msg = {
             'isSkip': '数据库查询{sql},\n数据库查询报错信息{msg}'.format(sql=sql,msg=traceback.format_exc()),
        }
        return msg

    count = len(date)
    if count != 0:
        msg = {
            'flag': False,
            'msg': {
                'expect': '期望结果 : {expect_message}'.format(expect_message='delete请求成功,删除资源相应资源'),
                'actual': '实际结果 : {expect_message}'.format(expect_message='delete请求失败,数据库中存在{id}'.format(id=date[0][0])),
                'sql': '数据查询sql : {sql}'.format(sql=sql),
                'sqlDate': '数据查询结果 : {date}'.format(date=date)
            }
        }
        return msg

    msg = {
        'flag': True
    }
    return msg



