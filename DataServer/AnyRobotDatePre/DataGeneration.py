#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 14:15
# @Author  : Evan.hu

from concurrent.futures import ThreadPoolExecutor
from entity import operation_logging
from entity.mysql_pool import select
from DataServer.AnyRobotDatePre.SqlRoute import SqlRule
from DataServer.AnyRobotSysGenDataFunction import CreateHost
from DataServer.AnyRobotSysGenDataFunction import CreateGroupHost
from DataServer.AnyRobotSysGenDataFunction import CreateAgentAuth
from DataServer.AnyRobotSysGenDataFunction import CreateInputAgentTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateInputFilebeatTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateInputWinlogbeatTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateOutputAgentTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateOutputFilebeatTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateOutputWinlogbeatTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateJobAgentTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateJobFilebeatTemplate
from DataServer.AnyRobotSysGenDataFunction import CreateJobWinlogbeatTemplate

log = operation_logging.TestLog().getlog()


class dataServer(object):
    """
    测试用例数据生成服务,服务初始化调用用于创建数据
    """
    def __init__(self):
        self.__count = 5
        self.__checklist = {
            'AuthID': CreateAgentAuth.GetAuth,
            'GroupID': CreateGroupHost.GetGroup,
            'HostID': CreateHost.GetHost,
            'InputAgentTemplate': CreateInputAgentTemplate.GetAgentTemplate,
            'InputFilebeatTemplate': CreateInputFilebeatTemplate.GetAgentTemplate,
            'InputWinlogbeatTemplate': CreateInputWinlogbeatTemplate.GetAgentTemplate,
            'OutputAgentTemplate': CreateOutputAgentTemplate.GetAgentTemplate,
            'OutputFilebeatTemplate': CreateOutputFilebeatTemplate.GetAgentTemplate,
            'OutputWinlogbeatTemplate': CreateOutputWinlogbeatTemplate.GetAgentTemplate,
            'WinlogbeatJobTemplate': CreateJobWinlogbeatTemplate.GetJobTemplate,
            'AgentJobTemplate': CreateJobAgentTemplate.GetJobTemplate,
            'FilebeatJobTemplate': CreateJobFilebeatTemplate.GetJobTemplate
        }

    def dataServerGen(self):
        # 初始化数据
        thread_pool = ThreadPoolExecutor(50)  # 定义5个线程执行此任务
        for key in self.__checklist.keys():
            sql = SqlRule(key)
            if not isinstance(sql,bool):
                date = select(sql)
                if len(date) < self.__count:
                    log.info("The data is create a data for {key}".format(key=key))
                    for count in range(1,self.__count + 1 -len(date)):
                        thread_pool.submit(self.__checklist.get(key))
                else:
                    log.info("The data is enough for {key}".format(key=key))

    def dataServerGen1(self):
        # 初始化数据
        thread_pool = ThreadPoolExecutor(50)  # 定义5个线程执行此任务
        for key in self.__checklist.keys():
            sql = SqlRule(key)
            if not isinstance(sql,bool):
                date = select(sql)
                if len(date) < self.__count:
                    log.info("The data is create a data for {key}".format(key=key))
                    for count in range(1,self.__count + 1 -len(date)):
                        thread_pool.submit(self.__checklist.get(key))
                else:
                    log.info("The data is enough for {key}".format(key=key))


if __name__ == '__main__':
    dataServer().dataServerGen()