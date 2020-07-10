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
    name = 'Apache日志采集' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    payload = {
        "category": "input",
        "config": {
            "encoding": "utf-8",
            "fields": '',
            "deadTime": 72,
            "paths": [
                "/log"
            ],
            "tail": False,
            "tags": [
                "MongoDB",
                "ElasticSearch"
            ],
            "tagsID": [
                5,
                6
            ],
            "type": "test",
            "cleanDeadEnable": True,
            "cleanDeadTime": 30,
            "maxLineByte": 100,
            "multiline": False,
            "multiline.pattern": "",
            "multiline.negate": False,
            "multiline.match": "after"
        },
        "agent": "AR-Agent",
        "description": "Apache日志采集Agent模板",
        "name": name
    }
    headers = header
    createResource(url, headers, payload, AssertContext)
    # flag = True
    # while flag:
    #     ResDate = createResource(url, headers, payload, AssertContext)
    #     if ResDate.get('flag') is None:
    #         assertContext = ResDate['AssertContext']
    #         if ResDate['response'].get(assertContext) is not None:
    #             return ResDate['response'][assertContext]
    #
    #     if ResDate['count'] >= 3:
    #         flag = False



if __name__ == '__main__':
    a = GetAgentTemplate()
    print(a)
