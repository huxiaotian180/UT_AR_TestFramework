#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 16:6
# @Author  : Evan.hu

from interface.public.isRepetition import isRep
from entity import operation_url
from entity.RequestsUtil import Request
from entity.preposition import prefix
import copy,os
path = os.path.split(os.path.abspath(__file__))

def PreviewUpload_post(info):
    """
        接口描述：上传文件预览
        接口请求url：url = "/manager/upload/preview/${id}/offset=0&limit=20"
        接口请求方法：post
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
        info = isRep(path,info,'PreviewUpload')

        if info['flag']:
            request = Request()
            request.post(url, headers, payload, info)

            info['log'].info("\n接口请求url:{url}\n接口请求header:{headers}\n接口请求body:{body}\n接口返回内容:{response}".format(
                url=info['url'], headers=info['headers'], body=info['payload'], response=info['response']))
            return info
    return info