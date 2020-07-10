#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 14:53
# @Author  : Evan.hu

from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetHost():
    AssertContext = 'hostId'
    url = "http://{ip}/manager/agents/host".format(ip=configManage().getIp)

    # 随机生成名称和IP
    name = 'linux' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    ip = '10.{ip1}.{ip2}.{ip3}'.format(ip1=random.randint(1, 99), ip2=random.randint(1, 99), ip3=random.randint(1, 99))
    payload = {
        "name": name,
        "ip": ip,
        "tags": [
            "Oracle"
        ],
        "systemType": "auto",
        "auths": [],
        "memoryLimit": 300,
        "description": "AnyRobot服务器主机",
        "tagsID": [
            1
        ],
        "system": ""
    }

    headers = header

    createResource(url, headers, payload, AssertContext)

if __name__ == '__main__':
    GetHost()
