#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 15:30
# @Author  : Evan.hu

from entity.mysql_pool import select
from entity.operation_json import OperetionJson
import traceback

def assertPut(info):
    # 获取接口请求body
    requestsBody = info['request_data']

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
    table = info['original_date']['verify']['putAssert']['table']
    id = info['original_date']['verify']['putAssert']['id']
    alterFiled = info['original_date']['verify']['putAssert']['alterText'].split(',')
    assertDb = info['original_date']['verify']['putAssert']['assertDb'].split(',')
    AssertKey = dict(zip(alterFiled, assertDb))

    # 获取验证信息
    Json = OperetionJson(requestsBody)
    for key in AssertKey.keys():

        # 获取请求参数中需要验证的参数
        requestsText = Json.get_value(key)  # 没找到是false
        if isinstance(requestsText, bool):
            msg = {
                'isSkip':'请求参数中不存在修改值 : {key}'.format(key = key)
            }
            return msg

        # 获取数据库信息
        sql = "select {field} from {table} where id ='{id}';".format(table=table, id=id, field=AssertKey[key])
        try:
            dateSql = select(sql)
        except Exception as e:
            msg = {
                'isSkip': '数据库查询失败 : \nsql={sql}\nmsg={msg}'.format(sql=sql,msg=traceback.format_exc())
            }
            return msg

        # 如果查询内容为空,表示数据库参数配置错误
        if len(dateSql) == 0:
            msg = {
                'isSkip': '数据库查询数据为空 : {sql}'.format(sql = sql)
            }
            return msg

        for context in dateSql:
            actualDb = '数据库查询信息 : 数据库信息 : {date}'.format(date=context[0])
            # 判断是否转化成数字
            isdigit = str(context[0]).isdigit()

            # 判断验证数据数据是否是int类型
            if isdigit:
                if str(requestsText[0]) == str(context[0]):
                    flag = True
                    actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key,value=requestsText[0])
                else:
                    flag = False
                    actualMsg = '实际结果 : 接口请求修改资源失败'

                # 返回断言结果
                msg = {
                    'except': {
                        'flag': isAlterFlag,
                        'msg': '{expect_message}'.format(expect_message=expectMsg)
                    },
                    'actual': {
                        'flag': flag,
                        'msg': '{actual_message}'.format(actual_message=actualMsg)
                    },
                    'db': {
                        'msg': '{actual_message}'.format(actual_message=actualDb)
                    }
                }
                return msg

            # 判断字符串是否能转化成字典和列表
            text = str(context[0]).strip()
            if len(text) == 0:    # 表示查询到的数据是空值
                if requestsText[0] == context[0]:
                    flag = True  # 修改成功
                    actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key,value=context[0])
                else:
                    flag = False  # 修改失败
                    actualMsg = '实际结果 : 接口请求修改资源失败'

                msg = {
                    'except': {
                        'flag': isAlterFlag,
                        'msg': '{expect_message}'.format(expect_message=expectMsg)
                    },
                    'actual': {
                        'flag': flag,
                        'msg': '{actual_message}'.format(actual_message=actualMsg)
                    },
                    'db': {
                        'msg': '{actual_message}'.format(actual_message=actualDb)
                    }
                }

                return msg

            elif text[0] == '{':  # 表示数据可以转换成字典形式
                # 判断是否可以转化成字典
                context1 = str(context[0]).replace('true', 'True')
                context2 = str(context1).replace('false', 'False')
                context3 = eval(context2)

                JsonDb = OperetionJson(context3)
                dbText = JsonDb.get_value(key)
                if dbText:
                    # 存在值
                    if requestsText[0] == dbText[0]:
                        # 修改成功
                        flag = True
                        actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key,value=dbText[0])
                    else:
                        # 修改失败
                        flag = False
                        actualMsg = '实际结果 : 接口请求修改资源失败'

                    msg = {
                        'except': {
                            'flag': isAlterFlag,
                            'msg': '{expect_message}'.format(expect_message=expectMsg)
                        },
                        'actual': {
                            'flag': flag,
                            'msg': '{actual_message}'.format(actual_message=actualMsg)
                        },
                        'db': {
                            'msg': '{actual_message}'.format(actual_message=actualDb)
                        }
                    }

                    return msg

                else:
                    # 数据查询失败,跳过测试
                    msg = {
                        'isSkip': '数据库查询验证字段{key}为空 : sql={sql}'.format(key = key,sql=sql)
                    }
                    return msg

            elif text[0] == '[':    # 判断是否转化成列表
                data1 = str(text).replace('true', 'True')
                data2 = str(data1).replace('false', 'False')
                if '{' in text:
                    data3 = eval(data2)
                    JsonDb = OperetionJson(data3)
                    dbText = JsonDb.get_value(key)
                    if dbText:
                        # 存在值
                        if requestsText[0] == dbText[0]:
                            # 修改成功
                            flag = True
                            actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key,value=dbText[0])
                        else:
                            # 修改失败
                            flag = False
                            actualMsg = '实际结果 : 接口请求修改资源失败'

                        msg = {
                            'except': {
                                'flag': isAlterFlag,
                                'msg': '{expect_message}'.format(expect_message=expectMsg)
                            },
                            'actual': {
                                'flag': flag,
                                'msg': '{actual_message}'.format(actual_message=actualMsg)
                            },
                            'db': {
                                'msg': '{actual_message}'.format(actual_message=actualDb)
                            }
                        }

                        return msg

                    else:
                        # 未查询到值,测试跳过
                        msg = {
                            'isSkip': '数据库查询验证字段{key}为空 : sql={sql}'.format(key = key,sql=sql)
                        }
                        return msg
                else:
                    date4 = eval(data2)

                    # 判断请求参数检验的字段是否也是list类型
                    if isinstance(requestsText[0],list):
                        diff1 = set(date4).difference(set(requestsText[0]))
                        diff2 = set(set(requestsText[0])).difference(date4)
                        if len(diff1) == 0 and len(diff2) == 0:
                            # 修改成功
                            flag = True
                            actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key,value=date4)
                        else:
                            # 修改失败
                            flag = False
                            actualMsg = '实际结果 : 接口请求修改资源成功'

                    else:
                        # 修改失败
                        flag = False
                        actualMsg = '实际结果 : 接口请求修改资源失败'

                    msg = {
                        'except': {
                            'flag': isAlterFlag,
                            'msg': '{expect_message}'.format(expect_message=expectMsg)
                        },
                        'actual': {
                            'flag': flag,
                            'msg': '{actual_message}'.format(actual_message=actualMsg)
                        },
                        'db': {
                            'msg': '{actual_message}'.format(actual_message=actualDb)
                        }
                    }

                    return msg

            else:
                if requestsText[0] == context[0]:
                    flag = True  # 修改成功
                    actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key,value=context[0])
                else:
                    flag = False  # 修改失败
                    actualMsg = '实际结果 : 接口请求修改资源失败'

                msg = {
                    'except': {
                        'flag': isAlterFlag,
                        'msg': '{expect_message}'.format(expect_message=expectMsg)
                    },
                    'actual': {
                        'flag': flag,
                        'msg': '{actual_message}'.format(actual_message=actualMsg)
                    },
                    'db': {
                        'msg': '{actual_message}'.format(actual_message=actualDb)
                    }
                }

                return msg