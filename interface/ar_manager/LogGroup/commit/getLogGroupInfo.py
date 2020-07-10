#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 16:16
# @Author  : Evan.hu

import requests
import json

from configuration.config import header
from configuration.configYaml import configManage
from entity.operation_json import OperetionJson

def getAllLogGroupIp():
    # 获取所有日志信息的Ip
    url = "http://{ip}/v1/search/fieldsAggs".format(ip=configManage().getIp)
    payload = {
        "filters": {
            "must": [
                {
                    "query_string": {
                        "analyze_wildcard": True,
                        "auto_generate_phrase_queries": True,
                        "query": "*"
                    }
                }
            ]
        },
        "indices": {
            "indexPattern": [],
            "manualIndex": []
        },
        "aggFields": [
            "host.keyword",
            "_type",
            "tags.keyword"
        ]
    }
    try:
        response = requests.request("POST", url, headers=header, data=json.dumps(payload))
        date = response.json()
        if isinstance(date, list) or isinstance(date, dict):
            a = OperetionJson(date)
            value = a.get_value('aggregations')
            if value:
                ip = value[0]['host.keyword']
                return ip
            else:
                return ''
        else:
            return ''
    except Exception as e:
        return ''

def getAllLogGroupType():
    # 获取系统里面全部日志组
    wareHouseId = {}
    url = "http://{ip}/api/v1/dataManager/logWareHouse?page=-1&size=-1&order=createTime&by=DESC".format(ip=configManage().getIp)
    try:
        response = requests.request("GET", url, headers=header)
        date = response.json()
        print(date)
        if isinstance(date, list) or isinstance(date, dict):
            for key in date['data']:
                a = OperetionJson(key)
                id = a.get_value('id')
                name = a.get_value('wareHouseName')
                type = a.get_value('dataType')
                if id:
                    GroupId = id[0]
                    wareHouseId[GroupId] = {}
                    wareHouseId[GroupId]['name'] = name[0]
                    wareHouseId[GroupId]['type'] = type[0]
            return wareHouseId
        else:
            return wareHouseId
    except Exception as e:
        return wareHouseId

def getLogGroupMapIpAndTags(wareHouseName):
    # 获取日志组type和ip之间的关系
    url = "http://{ip}/v1/search/fieldsAggs".format(ip=configManage().getIp)
    payload = {
        "filters": {
            "must": [
                {
                    "query_string": {
                        "analyze_wildcard": True,
                        "auto_generate_phrase_queries": True,
                        "query": "*"
                    }
                }
            ]
        },
        "indices": {
            "indexPattern": [
                wareHouseName
            ],
            "manualIndex": []
        },
        "aggFields": [
            "host.keyword",
            "_type",
            "tags.keyword"
        ]
    }

    response = requests.request("POST", url, headers=header, data=json.dumps(payload))
    try:
        date = response.json()
        if isinstance(date, list) or isinstance(date, dict):
            a = OperetionJson(date)
            value = a.get_value('aggregations')
            if value:
                ip = value[0]['host.keyword']
                tags = value[0]['tags.keyword']
                return ip, tags
            else:
                return '', ''
        else:
            return '', ''
    except Exception as e:
        return '',''

if __name__ == '__main__':
    date = '场景测试'
    date1 = getLogGroupMapIpAndTags(date)
    print(date1)