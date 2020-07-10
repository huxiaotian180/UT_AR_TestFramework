#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:45
# @Author  : Evan.hu
from DataServer.AnyRobotSysGenDataFunction import CreateInputAgentTemplate, CreateOutputAgentTemplate
from DataServer.AnyRobotSysGenDataFunction.commit.getInfo import createResource
from DataServer.AnyRobotSysGenDataFunction.commit.templateId import getUserId, getAgentInputTemplate, getAgentOutputTemplate
from configuration.config import header
import random
from configuration.configYaml import configManage


def GetJobTemplate():
    AssertContext = 'templateId'
    url = "http://{ip}/manager/agents/job/template".format(ip=configManage().getIp)
    name = 'Apache服务器任务' + '_' + str(random.randint(1, 99)) + '_' + str(random.randint(1, 999))
    AgentInputTemplate = getAgentInputTemplate()
    AgentOutputTemplate = getAgentOutputTemplate()
    if len(AgentInputTemplate) ==0:
        AgentInputTemplate = CreateInputAgentTemplate.GetAgentTemplate()
    if len(AgentOutputTemplate) ==0:
        AgentOutputTemplate = CreateOutputAgentTemplate.GetAgentTemplate()

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
        "agent": "AR-Agent",
        "category": "FileCollect",
        "schedule": {
            "type": "interval",
            "intervalTime": "10s",
            "period": "day",
            "days": 1,
            "startTime": "00:00"
        },
        "configInputTemplateIds": [
            AgentInputTemplate
        ],
        "configOutputTemplateIds": [
            AgentOutputTemplate
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
    #             flag = False
    #
    #     if ResDate['count'] >= 3:
    #         flag = False


if __name__ == '__main__':
    a = GetJobTemplate()
