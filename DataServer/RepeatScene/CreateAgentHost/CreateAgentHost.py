#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 10:59
# @Author  : Evan.hu


from entity.mysql_pool import select, update
from entity.operation_json import OperetionJson

class OperaCreateHost(object):
    def __init__(self,info,key):
        self.info = info
        self.key = key

    def OperaDbIp(self):
        # 获取请求参数的重复字段数据
        Json = OperetionJson(self.info['request_data'])
        flag = Json.get_value(self.key)
        if isinstance(flag, bool):  # 如果是布尔类型数据表示数据不存在，停止执行
            self.info['flag'] = False
            self.info['skipMeg'] = '重复场景mock----测试用例yaml文件设置重复参数错误'
            return self.info
        else:
            ip = flag[0]

        # 根据字段参数来查询数据库数据
        sql_select = "select id,ip from AgentHost limit 1;"
        data = select(sql_select)
        if len(data) == 0:
            self.info['flag'] = False
            self.info['skipMeg'] = '重复场景mock----数据无可用测试书记'
            return self.info
        else:
            id = data[0][0]
            # 更新数据数据
            update_sql = "update AgentHost set ip = '{ip}' where id= '{id}';".format(ip=ip, id=id)
            print(update_sql)
            update(update_sql)
            return self.info

    def OperaDbName(self):
        # 获取请求参数的重复字段数据
        Json = OperetionJson(self.info['request_data'])
        flag = Json.get_value(self.key)
        if isinstance(flag, bool):  # 如果是布尔类型数据表示数据不存在，停止执行
            self.info['flag'] = False
            self.info['skipMeg'] = '重复场景mock----测试用例yaml文件设置重复参数错误'
            return self.info
        else:
            name = flag[0]

        # 根据字段参数来查询数据库数据
        sql_select = "select id,name from AgentHost limit 1;"
        data = select(sql_select)
        if len(data) == 0:
            self.info['flag'] = False
            self.info['skipMeg'] = '重复场景mock----数据无可用测试书记'
            return self.info
        else:
            id = data[0][0]
            # 更新数据数据
            update_sql = "update AgentHost set name = '{name}' where id= '{id}';".format(name=name, id=id)
            print(update_sql)
            update(update_sql)
            return self.info

    def rule(self):
        if self.key == 'ip':
            return self.OperaDbIp()

        elif self.key == 'name':
            return self.OperaDbName()
        else:
            return True