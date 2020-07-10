#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:10
# @Author  : Evan.hu

from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetAgentTemplate():
    AssertContext = 'templateId'
    url = "http://{ip}/manager/agents/config/template".format(ip=configManage().getIp)
    name = 'Gitlab日志采集' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    payload = {
        "category": "input",
        "config": {
            "encoding": "plain",
            "exclude_lines": [],
            "fields": '',
            "ignore_older": 72,
            "include_lines": [],
            "paths": [
                "/log"
            ],
            "tail_files": False,
            "multiline": False,
            "multiline.pattern": "",
            "multiline.negate": False,
            "multiline.match": "after"
        },
        "agent": "Filebeat",
        "description": "Gitlab日志采集模板",
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