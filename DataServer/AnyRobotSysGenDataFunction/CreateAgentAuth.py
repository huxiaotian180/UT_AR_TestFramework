#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 13:49
# @Author  : Evan.hu

from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from DataServer.ParameterRouteServer.ParaDateFiled import ParaDateFiledServer
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetAuth():
    AssertContext = 'authId'
    url = "http://{ip}/manager/agents/auth".format(ip=configManage().getIp)
    headers = header
    # 随机生成主机组名称
    name = 'Auth' + '_' + str(random.randint(1, 999)) + '_' + str(random.randint(1, 999))
    ip = ParaDateFiledServer().getIp()
    payload = {"authName": name,
               "type": "ssh",
               "tags": ["MongoDB"],
               "config": {
                   "port": 22,
                   "name": "root",
                   "password": "eisoo.com123",
                   "testHost": ip
               },
               "tagsID": [5]
               }

    createResource(url, headers, payload, AssertContext)
    # flag = True
    # while flag:
    #     ResDate = createResource(url,headers,payload,AssertContext)
    #
    #     if ResDate.get('flag') is None:
    #         assertContext = ResDate['AssertContext']
    #         if ResDate['response'].get(assertContext) is not None:
    #             return ResDate['response'][assertContext]
    #
    #     if ResDate['count'] >= 3:
    #         flag = False

if __name__ == '__main__':
    GetAuth()