#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 15:53
# @Author  : Evan.hu

from DataServer.ParameterRouteServer.ParaDateAnyRobot import ParaDateAnyRobotServer
from DataServer.ParameterRouteServer.ParaDateFiled import ParaDateFiledServer
from DataServer.TransactionDate.logGroupInfo import LogGroup

def Merge(dict1, dict2):
    return (dict2.update(dict1))

def getParaSys():
    date = {
        'GroupID': ParaDateAnyRobotServer().getGroupID,
        'HostID': ParaDateAnyRobotServer().getHostID,
        'TemplateID': ParaDateAnyRobotServer().getTemplateID,
        'AuthID': ParaDateAnyRobotServer().getAuthID,
        'UserID': ParaDateAnyRobotServer().getUserID,
        'JobTemplateID': ParaDateAnyRobotServer().getJobTemplateID,
        'InputTemplateID': ParaDateAnyRobotServer().getInputTemplateID,
        'OutTemplateID': ParaDateAnyRobotServer().getOutTemplateID,
        'JobID': ParaDateAnyRobotServer().getJobID,
        'AgentInputTemplateID': ParaDateAnyRobotServer().getAgentInputTemplateID,
        'AgentOutTemplateID': ParaDateAnyRobotServer().getAgentOutTemplateID,
        'AgentJobTemplateID' : ParaDateAnyRobotServer().getAgentJobTemplateID,
        # 'indexList': '',
        # 'indexListDisplay': '',
        # 'streamId': '',
        'etcId': ParaDateAnyRobotServer().getEtlID,
        'logGroupIndex': LogGroup().getLogGroupIndex,
        'logGroupId': LogGroup().logGroupId,
        'logGroupHostIp': LogGroup().logGroupHostIp,
        'logGroupDataType': LogGroup().logGroupDataType,
        'logGroupHostTags': LogGroup().logGroupHostTags,
        'LogGroupIdPare': ParaDateAnyRobotServer().getParentGroupId,
        'logWareHouseId': ParaDateAnyRobotServer().getParentGroupId,
        'RoleId': ParaDateAnyRobotServer().getRoleId

    }
    return date

def getParaFiled():
    date = {
        'AnyRobotNameID': ParaDateFiledServer().getName,
        'Closed' : ParaDateFiledServer().getSwClosed,
        'Open' : ParaDateFiledServer().getSwOpen,
        'UUid': ParaDateFiledServer().getUUid ,
        'IpVR': ParaDateFiledServer().getIpVR,
        'IPError': ParaDateFiledServer().getIpError,
        'startTime': ParaDateFiledServer().getStartTime,
        'endTime': ParaDateFiledServer().getEndTime,
        'getEtlPortOld': ParaDateFiledServer().getEtlPortOld,
        'getEtlPortNew': ParaDateFiledServer().getEtlPortNew,
        'getEtlPortIll': ParaDateFiledServer().getEtlPortIll
    }
    return date

def default():
    return 1

def ParaRoute(key,index=''):
    """
    参数化入口函数，如果函数返回值中有0,1需要修改逻辑代码
    """
    switcher_filed = getParaFiled()
    switcher_sys = getParaSys()

    Merge(switcher_filed,switcher_sys)
    if len(index) == 0:
        date = switcher_sys.get(key,default)()
    else:
        try:
            date = switcher_sys.get(key,default)(index)
        except Exception as e:
            value = switcher_sys.get(key,default)()
            return value

    return date
if __name__ == '__main__':
    key = 'logGroupId'
    id = '08AUATtc'
    date = ParaRoute(key=key,index=id)
    print(id)