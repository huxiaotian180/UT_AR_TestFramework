#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 14:36
# @Author  : Evan.hu

from interface.public.isRepetition import isRep
from entity import operation_url
from entity.RequestsUtil import Request
from entity.preposition import prefix
import copy,os
path = os.path.split(os.path.abspath(__file__))

def SearchFieldValue_POST(info):
    """
        接口描述：获取当前搜索条件下某字段的值
        接口请求url：url = "/stream_manager/export_to_kafka/es_index?token=field_value"
        接口请求方法：POST
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
        info = isRep(path,info,'SearchFieldValue')

        if info['flag']:
            request = Request()
            request.post(url, headers, payload, info)

            info['log'].info("\n接口请求url:{url}\n接口请求header:{headers}\n接口请求body:{body}\n接口返回内容:{response}".format(
                url=info['url'], headers=info['headers'], body=info['payload'], response=info['response']))
            return info
    return info
