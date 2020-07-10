#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 10:18
# @Author  : Evan.hu

from assertContent.AssertRoute.AssertMapPutMethod.AssertPutRule import PutRule
from assertContent.AssertRoute.AssertMapDeleteMethod.AssertDeleteRule import DeleteRule
from assertContent.AssertRoute.AssertPostMethod.AssertPostMethod import PostRule
from assertContent.AssertRoute.AssertStatusCode.Assertstatus import StatusCode
from assertContent.AssertRoute.AssertResponseCode.AssertResponse import ResponseCode
from assertContent.AssertRoute.AssertGetCount.AssertGetCount import InfoCount
from assertContent.AssertRoute.AssertGetId.AssertGetId import InfoId
from assertContent.AssertRoute.AssertGetAll.AssertGetAll import InfoAll

def default():
    # info['flag'] = False
    # info['skipMeg'] = '重复场景mock----接口注册参数不存在'
    # return info
    pass

def AssertRule(type,id='',key='',value='',db='',flag=''):
    switcher = {
        0: StatusCode(value).GetStatusCode,
        1 :ResponseCode(key,value,flag).GetResponseCode,
        2: PostRule(key,value).GetPostRule,
        3: DeleteRule(id,db).GetDelete,
        4: PutRule(id,key,value,db).GetPut,
        5: InfoCount(key,db).GetCount,
        6: InfoId(key,db,id).GetId,
        7: InfoAll(key,db).GetAll

    }
    if switcher.get(type) is not None:
        return switcher.get(type)()
    else:
        return default()


if __name__ == '__main__':
    # date = AssertRule(type=4,id='TemplateID',key='ip',value=12)
    date = AssertRule(type=4, id='TemplateID', key='ip', value=12,db="a,e")
    print(date)