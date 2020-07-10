#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 15:55
# @Author  : Evan.hu

import requests
from configuration.config import header
from configuration.configYaml import configManage
from entity.operation_json import OperetionJson

def getEtlPort():
    url = "http://{ip}/etl/input/list?start=0&limit=-1".format(ip=configManage().getIp)
    payload = {}
    headers = header
    response = requests.request("GET", url, headers=headers, data=payload)
    date = response.json()
    a = OperetionJson(date)
    value = a.get_value('port')
    if value:
        return value
    else:
        return []

def getEtlId():
    url = "http://{ip}/etl/input/list?start=0&limit=-1".format(ip=configManage().getIp)
    payload = {}
    headers = header
    response = requests.request("GET", url, headers=headers, data=payload)
    date = response.json()
    a = OperetionJson(date)
    value = a.get_value('id')
    if value:
        return value
    else:
        return []

def getEtlIdInfo(url,key):
    payload = {}
    headers = header
    response = requests.request("GET", url, headers=headers, data=payload)
    date = response.json()
    a = OperetionJson(date)
    value = a.get_value(key)
    if value:
        return value[0]

if __name__ == '__main__':
    url = "http://192.168.84.26:80/etl/input/f30b55ce-af82-11ea-873a-5681e6345b9c"
    date = getEtlIdInfo(url,'port')
    print(date)