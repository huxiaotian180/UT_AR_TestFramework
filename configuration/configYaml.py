#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 17:15
# @Author  : Evan.hu

import os
from entity.operationYaml import operationRead


class configManage(object):

    def configRead(self):
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'configuration'
        name = 'config.yaml'
        return operationRead(path,name)
    @property
    def getIp(self):
        date = self.configRead()
        return date['TestEnv']['ip']

    @property
    def getPort(self):
        date = self.configRead()
        return date['TestEnv']['port']



if __name__ == '__main__':
    date1 = configManage().getIp
    print(date1)