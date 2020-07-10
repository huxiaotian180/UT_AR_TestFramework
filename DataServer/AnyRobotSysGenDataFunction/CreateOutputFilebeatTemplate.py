#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:11
# @Author  : Evan.hu

from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetAgentTemplate():
    AssertContext = 'templateId'
    url = "http://{ip}/manager/agents/config/template".format(ip=configManage().getIp)
    name = 'GitLib日志采集输出' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    ip = '10.{ip1}.{ip2}.{ip3}'.format(ip1=random.randint(1, 99), ip2=random.randint(1, 99), ip3=random.randint(1, 99))
    payload = {
        "description": "GitLib日志采集输出模板",
        "category": "output",
        "config": {
            "hosts": [
                ip
            ],
            "type": "Logstash"
        },
        "agent": "Filebeat",
        "name": name
    }
    headers = header
    createResource(url, headers, payload, AssertContext)

    # flag = True
    # while flag:
    #     ResDate = createResource(url, headers, payload, AssertContext)
    #     print(ResDate)
    #     if ResDate.get('flag') is None:
    #         assertContext = ResDate['AssertContext']
    #         if ResDate['response'].get(assertContext) is not None:
    #             return ResDate['response'][assertContext]
    #
    #     if ResDate['count'] >= 3:
    #         flag = False


if __name__ == '__main__':
    a = GetAgentTemplate()