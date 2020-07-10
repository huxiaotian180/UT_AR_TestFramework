#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 16:47
# @Author  : Evan.hu

from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetGroup():
    AssertContext = 'groupId'
    url = "http://{ip}/manager/agents/hostgroup".format(ip=configManage().getIp)
    # 随机生成主机组名称
    name = 'hu' + '_' + str(random.randint(1, 999)) + '_' + str(random.randint(1, 999))
    payload = {
        "name": name,
        "hosts": [],
        "whitelist": [
            "MongoDB",
            "SQLServer"],
        "templateIds": [],
        "description": "GitLab服务器收集主机组",
        "tagsID": [
            5,
            4
        ]
    }
    headers = header
    createResource(url, headers, payload, AssertContext)

    # flag = True
    # while flag:
    #     ResDate = createResource(url, headers, payload, AssertContext)
    #
    #     if ResDate.get('flag') is None:
    #         assertContext = ResDate['AssertContext']
    #         if ResDate['response'].get(assertContext) is not None:
    #             return ResDate['response'][assertContext]
    #
    #     if ResDate['count'] >= 3:
    #         flag = False
