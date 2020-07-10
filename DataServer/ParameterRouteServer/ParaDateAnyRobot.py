#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 16:03
# @Author  : Evan.hu

from entity.mysql_pool import select
import random
from interface.ar_manager.etl.commit.getEtlInfo import getEtlId


class ParaDateAnyRobotServer(object):
    # def __init__(self,info):
    #     self.info = info
    """
    生成接口字段参数
    """

    def getUserID(self):
        sql = 'select userId from User where loginName = "admin";'
        date = select(sql)
        if len(date) > 0:
            for value in date:
                UserID = value[0]
            return UserID
        return 0

    def getJobTemplateID(self):
        # date = random.choices(DateList)
        JobTemplateID = []
        sql = 'select id from AgentJobTemplate;'
        date = select(sql)
        if len(date) == 0:
            return 0
        for value in date:
            JobTemplateID.append(value[0])
        JobID = random.choices(JobTemplateID)
        return JobID[0]

    def getInputTemplateID(self):
        sql = "select id from AgentConfigTemplate where category = 'input';"
        InputTemplateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            InputTemplateID.append(id[0])
        ID = random.choices(InputTemplateID)

        return ID[0]

    def getOutTemplateID(self):
        sql = "select id from AgentConfigTemplate where category = 'output';"
        OutputTemplateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            OutputTemplateID.append(id[0])
        ID = random.choices(OutputTemplateID)

        return ID[0]

    def getJobID(self):
        sql = "select id from AgentJobInfo;"
        OutputTemplateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            OutputTemplateID.append(id[0])
        ID = random.choices(OutputTemplateID)

        return ID[0]

    def getGroupID(self):
        sql = "select id from AgentGroup;"
        groupID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            groupID.append(id[0])
        ID = random.choices(groupID)

        return ID[0]

    def getHostID(self):
        sql = "select id from AgentHost;"
        hostID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            hostID.append(id[0])
        ID = random.choices(hostID)

        return ID[0]

    def getTemplateID(self):
        sql = "select id from AgentConfigTemplate;"
        templateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            templateID.append(id[0])
        ID = random.choices(templateID)

        return ID[0]

    def getAuthID(self):
        sql = "select id from AgentHostAuth;"
        authID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            authID.append(id[0])
        ID = random.choices(authID)
        return ID[0]

    def getAgentInputTemplateID(self):
        sql = "select id from AgentConfigTemplate where agent='AR-Agent' and category='input';"
        templateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            templateID.append(id[0])
        ID = random.choices(templateID)

        return ID[0]


    def getAgentOutTemplateID(self):
        sql = "select id from AgentConfigTemplate where agent='AR-Agent' and category='output';"
        InputTemplateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            InputTemplateID.append(id[0])
        ID = random.choices(InputTemplateID)

        return ID[0]

    def getAgentJobTemplateID(self):
        JobTemplateID = []
        sql = "select id from AgentJobTemplate where agent='AR-Agent';"
        date = select(sql)
        if len(date) == 0:
            return 0
        for value in date:
            JobTemplateID.append(value[0])
        JobID = random.choices(JobTemplateID)
        return JobID[0]

    def getEtlID(self):
        date = getEtlId()
        if len(date) == 0:
            return 0
        else:
            id = random.choice(date)
            return id


    def getParentGroupId(self):
        sql = "select groupId from LogGroup;"
        templateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            templateID.append(id[0])
        ID = random.choices(templateID)

        return ID[0]


    def getLogWareHouseId(self):
        sql = "select id from LogWareHouse;"
        templateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            templateID.append(id[0])
        ID = random.choices(templateID)

        return ID[0]

    def getRoleId(self):
        sql = "select roleId from Role where roleName != 'admin';"
        templateID = []
        date = select(sql)
        if len(date) == 0:
            return 0
        for id in date:
            templateID.append(id[0])
        ID = random.choices(templateID)
        return ID[0]

if __name__ == '__main__':
    date = ParaDateAnyRobotServer().getRoleId()
    print(date)