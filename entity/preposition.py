#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 14:26
# @Author  : Evan.hu

# 根据参数判断函数是否需要参数化
import copy,traceback,re
from configuration.config import header
from DataServer.ParameterRouteServer.ParameterRoute import ParaRoute
from entity import opertation_file
from entity.mysql_pool import select


def parse(date):
    rule1 = re.compile(r'\$\{(\w*)\}\$')
    pareDate = rule1.findall(str(date))
    date = set(pareDate)
    dateList = list(date)
    return dateList

class prefix(object):
    def __init__(self,info):
        self.info = info

    # 用于处理参数化数据
    def Parameter(self):
        # 判断是否存在header,加入header
        headers = header
        flag = self.info['Requests'].get('header')
        if flag is not None:
            req_header = self.info['Requests']['header']
            for key in req_header.keys():
                headers[key] = req_header[key]

        self.info['Headers'] = headers

        # 解析脚本中的参数化数据
        datePare = parse(self.info)
        if len(datePare) > 0:
            flagParameter = True
        else:
            flagParameter = False

        # 参数化标志
        if flagParameter:
            parameter_list = {}

            # 参数化字段
            key = datePare
            # 判断是否存在事务类型参数化
            transactionId,getIndex = '',''
            if self.info.get('transaction') is not None:
                transactionId = self.info['transaction']
                getIndex = ParaRoute(transactionId)
                if getIndex == 0:
                    self.info['flag'] = False
                    self.info['skipMeg'] = '接口数据参数化服务---->测试用例存在参数化数据未注册: {key}'.format(key=self.info['transaction'])
                    return self.info

                if len(str(getIndex)) == 0:
                    self.info['flag'] = False
                    self.info['skipMeg'] = '接口事务数据参数化服务---->测试数据为空,跳过测试: {key}'.format(key=self.info['transaction'])
                    return self.info
            for value in key:
                try:
                    # 调用参数化路由服务
                    if len(transactionId) == 0:
                        date = ParaRoute(key=value)
                    else:
                        date = ParaRoute(key=value,index=getIndex)

                    if date == 0:
                        self.info['flag'] = False
                        self.info['skipMeg'] = '接口数据参数化服务---->测试数据为空,跳过测试: {key}'.format(key=value)
                        break

                    if date == 1:
                        self.info['flag'] = False
                        self.info['skipMeg'] = '接口数据参数化服务---->测试用例存在参数化数据未注册: {key}'.format(key=value)
                        break

                    parameter_list[value] = date

                except Exception as e:
                    traceback.print_exc()
                    msg = traceback.format_exc()
                    self.info['log'].info(msg)
                    self.info['flag'] = False
                    self.info['skipMeg'] = '接口数据参数化服务异常: {msg}'.format(msg=msg)
                    return self.info

            # 调用参数化脚本数据
            try:
                data = opertation_file.get_parameter(self.info, parameter_list)
                data['parameterize'] = parameter_list
                log = data.pop('log')
                info = copy.deepcopy(data)
                info['log'] = log
                return info
            except Exception as e:
                msg = traceback.format_exc()
                self.info['flag'] = False
                self.info['skipMeg'] = msg

        return self.info

    def getPutDate(self,info):
        # 获取接口断言相关字段
        type = info['original_date']['verify']['AssertType'][0]

        if type==4:
            table = info['original_date']['verify']['putAssert']['table']
            id = info['original_date']['verify']['putAssert']['id']
            alterFiled = info['original_date']['verify']['putAssert']['alterText'].split(',')
            assertDb = info['original_date']['verify']['putAssert']['assertDb'].split(',')
            AssertKey = dict(zip(alterFiled, assertDb))

            for key in AssertKey.keys():
                sql = "select {field} from {table} where id ='{id}';".format(table=table, id=id, field=AssertKey[key])

                try:
                    dateSql = select(sql)

                    if len(dateSql) == 0:
                        info['flag'] = False
                        info['skipMeg'] = '数据库查询数据为空:{msg}'.format(msg=sql)
                        return info

                    # 数据信息保存
                    date = {
                        'dbTest_before': dateSql[0][0],
                        'sql': sql
                    }
                    info['assertPutInfo'] = date
                    return info

                except Exception as e:
                    msg = traceback.format_exc()
                    info['flag'] = False
                    info['skipMeg']= msg
                    return info
        else:
            return info

    def function(self):
        info= self.Parameter()
        info = self.getPutDate(info)
        return info
