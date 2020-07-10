#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 15:3
# @Author  : Evan.hu

from interface.public.isRepetition import isRep
from entity import operation_url
from entity.RequestsUtil import Request
from entity.preposition import prefix
import copy,os
path = os.path.split(os.path.abspath(__file__))

def GetLogLibraryMapInformation_GET(info):
    """
        接口描述：获取日志库映射信息
        接口请求url：url = "/api/v1/dataManager/logWareHouse/${id}$/indices"
        接口请求方法：GET
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
        info = isRep(path,info,'GetLogLibraryMapInformation')

        if info['flag']:
            request = Request()
            request.get(url, headers, payload, info)

            info['log'].info("\n接口请求url:{url}\n接口请求header:{headers}\n接口请求body:{body}\n接口返回内容:{response}".format(
                url=info['url'], headers=info['headers'], body=info['payload'], response=info['response']))
            return info
    return info
