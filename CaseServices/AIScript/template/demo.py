#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 11:15
# @Author  : Evan.hu

from entity.operation_json import OperetionJson
from entity.mysql_pool import select

result = {}
sql = "select name,id from AgentHostAuth where name = 'Auth_54_509';"
date = select(sql)

filed = ['name','id']
for text in date:
    for date in zip(filed,text):
        result[date[0]] = date[1]

print(result)