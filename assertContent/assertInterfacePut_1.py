#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 11:19
# @Author  : Evan.hu

from entity.mysql_pool import select
from entity.operation_json import OperetionJson
import traceback

def dataStructure(dbDate,key):
    # 判断是否可以转化成数值
    isdigit = str(dbDate).isdigit()

    if isdigit:
        return dbDate

    elif dbDate[0] == '{':
        # 数据是字典类型,查找到对应的数值
        try:
            value = eval(dbDate)
        except Exception as e:
            context1 = str(dbDate).replace('true', 'True')
            context2 = str(context1).replace('false', 'False')
            value = eval(context2)

        JsonDb = OperetionJson(value)
        dbText = JsonDb.get_value(key)
        if dbText:
            return dbText[0]
        else:
            msg = {
                'isSkip': '数据库信息不存在验证字段{key} : date={date}'.format(key=key, date=dbDate)
            }
            return msg

    elif dbDate[0] == '[':
        if '{' in dbDate:
            # 如果数据类型是list类型中包含dict类型,查找对应的key值
            try:
                value = eval(dbDate)
            except Exception as e:
                context1 = str(dbDate).replace('true', 'True')
                context2 = str(context1).replace('false', 'False')
                value = eval(context2)

            JsonDb = OperetionJson(value)
            dbText = JsonDb.get_value(key)
            if dbText:
                return dbText[0]
            else:
                msg = {
                    'isSkip': '数据库信息不存在验证字段{key} : date={date}'.format(key=key, date=dbDate)
                }
                return msg

        # 如果数据类型是list直接返回
        try:
            value = eval(dbDate)
        except Exception as e:
            context1 = str(dbDate).replace('true', 'True')
            context2 = str(context1).replace('false', 'False')
            value = eval(context2)

        return value

    else:
        # 以上判断都不通过则表示数据类型是str
        return dbDate


def assertContext(reqDate,dbDate,key):
    date = dataStructure(dbDate,key)

    if isinstance(date,dict):
        if date.get('isSkip') is not None:
            return date

    if isinstance(reqDate,list) and isinstance(date,list):
        diff1 = set(reqDate).difference(set(date))
        diff2 = set(set(date)).difference(reqDate)
        if len(diff1) == 0 and len(diff2) == 0:
            # 修改成功
            flag = True
            actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key, value=reqDate)
        else:
            # 修改失败
            flag = False
            actualMsg = '实际结果 : 接口请求修改资源失败'

    elif isinstance(reqDate,dict) and isinstance(date,dict):
        if reqDate == date:
            flag = True
            actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key, value=reqDate)
        else:
            flag = False
            actualMsg = '实际结果 : 接口请求修改资源失败'

    else:
        if str(reqDate) == str(date):
            flag = True
            actualMsg = '实际结果 : 接口请求修改资源成功,{key}={value}'.format(key=key, value=reqDate)
        else:
            flag = False
            actualMsg = '实际结果 : 接口请求修改资源失败'

    msg = {
        'actual': {
            'flag': flag,
            'msg': actualMsg
        }
    }

    return msg

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

        # 接口验证
        assertDate = assertContext(requestsText[0],dateSql[0][0],key)
        if assertDate.get('isSkip') is not None:
            return assertDate

        else:
            msg = {
                'except': {
                    'flag': isAlterFlag,
                    'msg': '{expect_message}'.format(expect_message=expectMsg)
                },
                'db': {
                    'msg': '数据库查询信息{db_message}'.format(db_message=dateSql[0][0])
                }
            }
            msg['actual'] = assertDate['actual']
            return msg


if __name__ == '__main__':
    reqDate = {"a":"abc","b":"abc1"}
    key = 'maxLineByte'
    dbDate = '{"multiline.pattern": "", "maxLineByte": {"a":"abc","b":"abc"}, "tagsID": [2, 4], "multiline.negate": false, "encoding": "utf-8", "fields": "", "multiline.match": "after", "tail": false, "cleanDeadTime": 30, "multiline": false, "deadTime": 24, "paths": [], "cleanDeadEnable": true, "type": "test", "tags": ["MySQL", "SQLServer"]}'

    date = assertContext(reqDate,dbDate,key)
    print(date)
