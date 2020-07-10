#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 16:58
# @Author  : Evan.hu

import random
from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from configuration.configYaml import configManage


def GetMysqlDb():
    AssertContext = 'DBConnectId'
    url = "http://{ip}/manager/dbconnect".format(ip=configManage().getIp)
    name = 'mysql' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    ip = '10.{ip1}.{ip2}.{ip3}'.format(ip1=random.randint(1, 99), ip2=random.randint(1, 99), ip3=random.randint(1, 99))
    payload = {
        "type": "mysql",
        "config": {
            "host": ip,
            "port": 3306,
            "user": "root",
            "password": "eisoo.com",
            "sid": "AnyRobot",
            "charset": "utf8"
        },
        "id": "",
        "name": name
    }

    headers = {
        'Content-Type': 'application/json'
    }
    flag = True
    while flag:
        ResDate = createResource(url, headers, payload, AssertContext)
        print(ResDate)

        if ResDate.get('flag') is None:
            assertContext = ResDate['AssertContext']
            if ResDate['response'].get(assertContext) is not None:
                return ResDate['response'][assertContext]

        if ResDate['count'] >= 3:
            flag = False

if __name__ == '__main__':
    a = GetMysqlDb()