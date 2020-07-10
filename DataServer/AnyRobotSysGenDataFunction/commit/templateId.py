#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 11:05
# @Author  : Evan.hu
from entity.mysql_pool import select
import time,random

def getTemplate(sql):
    # 获取Agent模板
    templateList = []
    count = 1
    flag = True
    while flag and count <= 4:
        sqlUser = sql
        try:
            data = select(sqlUser)
            if len(data) > 0:
                for date in data:
                    templateList.append(date[0])
                AgentInputTemplate = random.choices(templateList)[0]
                flag = False
                return AgentInputTemplate
            else:
                count = count + 1
                time.sleep(2)
        except Exception as e:
            print(e)
            count = count + 1
            time.sleep(2)

def getUserId():
    # 获取用户信息
    count = 1
    flag = True
    while flag and count <= 4:
        sqlUser = "select userId from User where loginName='admin';"
        try:
            data = select(sqlUser)
            userId = data[0][0]
            flag = False
            return userId
        except Exception as e:
            print(e)
            count = count + 1
            time.sleep(2)

def getAgentInputTemplate():
    # 获取Agent模板
    sqlUser = "select id from AgentConfigTemplate where agent='AR-Agent' and category = 'input';"
    return getTemplate(sqlUser)

def getFilebeatInputTemplate():
    # 获取Agent模板
    sqlUser = "select id from AgentConfigTemplate where agent='Filebeat' and category = 'input';"
    return getTemplate(sqlUser)

def getWinlogbeatInputTemplate():
    # 获取Agent模板
    sqlUser = "select id from AgentConfigTemplate where agent='Winlogbeat' and category = 'input';"
    return getTemplate(sqlUser)

def getAgentOutputTemplate():
    # 获取Agent模板
    sqlUser = "select id from AgentConfigTemplate where agent='AR-Agent' and category = 'output';"
    return getTemplate(sqlUser)

def getFilebeatOutputTemplate():
    sqlUser = "select id from AgentConfigTemplate where agent='Filebeat' and category = 'output';"
    return getTemplate(sqlUser)

def getWinlogbeatOutputTemplate():
    # 获取Agent模板
    sqlUser = "select id from AgentConfigTemplate where agent='Winlogbeat' and category = 'output';"
    return getTemplate(sqlUser)


if __name__ == '__main__':
    date = getFilebeatOutputTemplate()
    print(date)