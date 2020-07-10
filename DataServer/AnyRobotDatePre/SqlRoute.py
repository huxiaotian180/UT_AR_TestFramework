#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 14:23
# @Author  : Evan.hu

def SqlRule(key):
    """
    对应数据服务的sql语句注册
    :param key:
    :return:
    """
    switcher = {
        'AuthID': 'select id from AgentHostAuth;',
        'GroupID': 'select id from AgentGroup;',
        'HostID': 'select id from AgentHost;',
        'InputAgentTemplate': "select id from AgentConfigTemplate where agent='AR-Agent' and category = 'input';",
        'InputFilebeatTemplate': "select id from AgentConfigTemplate where agent='Filebeat' and category = 'input';",
        'InputWinlogbeatTemplate': "select id from AgentConfigTemplate where agent='Winlogbeat' and category = 'input';",
        'OutputAgentTemplate': "select id from AgentConfigTemplate where agent='AR-Agent' and category = 'output';",
        'OutputFilebeatTemplate': "select id from AgentConfigTemplate where agent='Filebeat' and category = 'output';",
        'OutputWinlogbeatTemplate': "select id from AgentConfigTemplate where agent='Winlogbeat' and category = 'output';",
        'AgentJobTemplate': "select id from AgentJobTemplate where agent='AR-Agent';",
        'FilebeatJobTemplate': "select id from AgentJobTemplate where agent='Filebeat';",
        'WinlogbeatJobTemplate': "select id from AgentJobTemplate where agent='Winlogbeat';"

    }
    if switcher.get(key) is not None:
        return switcher[key]
    else:
        return False
