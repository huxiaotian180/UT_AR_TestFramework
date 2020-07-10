#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 9:46
# @Author  : Evan.hu
from DataServer.RepeatScene.AlterHost.AlterAgentHost import OperaAlterHost
from DataServer.RepeatScene.AlterAgentTemplate.AlterAgentTemplate import OperaAlterTemplate
from DataServer.RepeatScene.CreateAgentHost.CreateAgentHost import OperaCreateHost
from DataServer.RepeatScene.CreateAgentHostGroup.CreateHostGroup import OperaCreateHostGroup
from DataServer.RepeatScene.AddAgentTemplate.AddAgentTemplate import OperaCreateAgentTemplate
from DataServer.RepeatScene.AlterAgentJobTemplateInfo.AlterAgentJobTemplate import OperaAlterAgentJobTemplate
from DataServer.RepeatScene.CreateAgentJobTemplate.CreateAgentJobTemplate import OperaCreateAgentJobTemplate
from DataServer.RepeatScene.CreateAgentOutTemplate.CreateAgentOutTemplate import OperaCreateAgentOutTemplate
def default(interface,key,info):
    info['flag'] = False
    info['skipMeg'] = '幂等性服务---->函数未注册:接口{interface}'.format(interface=interface)
    return info

def RpRoute(interface,key,info):
    switcher = {
        'AlterAgentHost': OperaAlterHost(info,key).rule,
        'AlterAgentTemplate' : OperaAlterTemplate(info,key).rule,
        'CreateAgentHost': OperaCreateHost(info,key).rule,
        'CreateAgentHostGroup': OperaCreateHostGroup(info,key).rule,
        'AddAgentTemplate' : OperaCreateAgentTemplate(info,key).rule,
        'AlterAgentJobTemplateInfo' : OperaAlterAgentJobTemplate(info,key).rule,
        'CreateAgentJobTemplate' : OperaCreateAgentJobTemplate(info,key).rule,
        'CreateAgentOutTemplate' : OperaCreateAgentOutTemplate(info,key).rule
    }
    if switcher.get(interface) is not None:
        date = switcher.get(interface)()
        if isinstance(date,bool):
            info['flag'] = False
            info['skipMeg'] = '幂等性服务---->接口函数字段未注册:接口{interface}字段{key}'.format(interface=interface, key=key)
            return info
        return date
    else:
        return default(interface,key,info)


if __name__ == '__main__':
    date = RpRoute('Agent','ip',info={})
    print(date)