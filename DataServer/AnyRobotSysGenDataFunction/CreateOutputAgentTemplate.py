#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:07
# @Author  : Evan.hu

from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetAgentTemplate():
    AssertContext = 'templateId'
    url = "http://{ip}/manager/agents/config/template".format(ip=configManage().getIp)
    name = 'Apache日志采集输出' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    payload = {
        "description": "Apache日志采集输出模板",
        "category": "output",
        "config": {
            "port": "23",
            "ip": "11.1.11.1",
            "agentProtocol": "HTTP",
            "speed": {
                "period": {
                    "date": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "startTime": "03:03:03",
                    "endTime": "23:59:59",
                    "unit": "day"
                },
                "type": "bandwidth",
                "value": "2MB/S",
                "limitSpeed": True
            }
        },
        "agent": "AR-Agent",
        "name": name
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


if __name__ == '__main__':
    a = GetAgentTemplate()