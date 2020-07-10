#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 17:22
# @Author  : Evan.hu

from interface.public.isRepetition import isRep
from entity import operation_url
from entity.RequestsUtil import Request
from entity.preposition import prefix
import copy,os
path = os.path.split(os.path.abspath(__file__))

def DBIOMoveEntity_put(info):
    """
        接口描述：移动实体
        接口请求url：url = "/manager/dbio/entityManager/entities/entity/${entityID}$"
        接口请求方法：put
    """
    # 接口前置判断
    date = prefix(info).function()
    if info['flag']:
        log = date.pop('log')
        info = copy.deepcopy(date)
        info['log'] = log
        url = operation_url.url(info['urlParameter'])
        headers = info['Headers']
        payload = info['request_data']
        info = isRep(path,info,'DBIOMoveEntity')

        if info['flag']:
            request = Request()
            request.put(url, headers, payload, info)

            info['log'].info("\n接口请求url:{url}\n接口请求header:{headers}\n接口请求body:{body}\n接口返回内容:{response}".format(
                url=info['url'], headers=info['headers'], body=info['payload'], response=info['response']))
            return info
    return info