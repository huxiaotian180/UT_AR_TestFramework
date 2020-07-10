#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:46
# @Author  : Evan.hu
from DataServer.AnyRobotSysGenDataFunction import CreateInputWinlogbeatTemplate,CreateOutputWinlogbeatTemplate
from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from DataServer.AnyRobotSysGenDataFunction.commit.templateId import getUserId, getWinlogbeatInputTemplate,getWinlogbeatOutputTemplate
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetJobTemplate():
    AssertContext = 'templateId'
    url = "http://{ip}/manager/agents/job/template".format(ip=configManage().getIp)
    name = 'Apache服务器任务' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    WinlogbeatInputTemplate = getWinlogbeatInputTemplate()
    WinlogbeatOutputTemplate = getWinlogbeatOutputTemplate()

    if len(WinlogbeatInputTemplate) == 0:
        WinlogbeatInputTemplate = CreateInputWinlogbeatTemplate.GetAgentTemplate()

    if len(WinlogbeatOutputTemplate) == 0:
        WinlogbeatOutputTemplate = CreateOutputWinlogbeatTemplate.GetAgentTemplate()
    payload = {
        "name": name,
        "tagsID": [
            5,
            4
        ],
        "tags": [
            "MongoDB",
            "SQLServer"
        ],
        "agent": "Winlogbeat",
        "category": "FileCollect",
        "schedule": {
            "type": "interval",
            "intervalTime": "10s",
            "period": "day",
            "days": 1,
            "startTime": "00:00"
        },
        "configInputTemplateIds": [
            WinlogbeatInputTemplate
        ],
        "configOutputTemplateIds": [
            WinlogbeatOutputTemplate
        ],
        "configGroupIds": [],
        "configHostIds": [],
        "description": "Apache服务器任务模板"
    }
    headers = header
    userId = getUserId()
    if userId is not None:
        headers['user'] = userId

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
    a = GetJobTemplate()