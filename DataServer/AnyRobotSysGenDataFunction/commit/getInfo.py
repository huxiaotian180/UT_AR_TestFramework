#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 15:39
# @Author  : Evan.hu

from entity.DecoratorCount import Counter
import json,requests

# @Counter
def createResource(url,headers,payload,AssertContext,*args, **kwargs):
    requests.request("POST", url, headers=headers, data=json.dumps(payload))
    # resData = {
    #     'AssertContext': AssertContext
    # }
    # response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    # if response.status_code == 200:
    #     try:
    #         date = response.json()
    #         resData['response'] = date
    #         return resData
    #     except Exception as e:
    #         date = response.text
    #         try:
    #             date = eval(date)
    #             resData['response'] = date
    #             return resData
    #         except Exception as e:
    #             resData['flag'] = False
    #             return resData
    #
    # else:
    #     resData['flag'] = False
    #     return resData
