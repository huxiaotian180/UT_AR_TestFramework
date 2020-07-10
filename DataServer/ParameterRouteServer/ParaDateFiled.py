#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 16:03
# @Author  : Evan.hu

import time
import random, uuid
from interface.ar_manager.etl.commit.getEtlInfo import getEtlPort


class ParaDateFiledServer(object):
    # def __init__(self,info):
    #     self.info = info
    """
    生成接口字段参数
    """

    def getName(self):
        name = str(random.choice(range(10, 999))) + '_' + str(random.choice(range(10, 999)))
        return name

    def getSwClosed(self):
        return 'disable'

    def getSwOpen(self):
        return 'enable'

    def getIp(self):
        ipList = ["192.168.84.105",
                  "192.168.84.192",
                  "192.168.84.217",
                  "192.168.84.108",
                  "192.168.84.107",
                  "192.168.84.182",
                  "192.168.84.193",
                  "192.168.84.109",
                  "192.168.84.175",
                  "192.168.84.60",
                  "192.168.84.61",
                  "192.168.84.63",
                  "192.168.84.62",
                  "192.168.84.64",
                  "192.168.84.65",
                  "192.168.84.66"]
        return random.choice(ipList)

    def getPort(self):
        # 系统合法参数 20010-20099、162，514，5140
        portList = [port for port in range(20010, 20100)]
        portList.append(162)
        portList.append(514)
        portList.append(5140)
        port = random.choice(portList)
        return port

    def getIpVR(self):
        return '{ip1}.{ip2}.{ip3}.{ip4}'.format(ip1=10, ip2=random.choice(range(10, 250)),
                                                ip3=random.choice(range(10, 250)), ip4=random.choice(range(10, 250)))

    def getIpError(self):
        return '{ip1}.{ip2}.{ip3}.{ip4}'.format(ip1='abc', ip2=random.choice(range(10, 99)),
                                                ip3=random.choice(range(10, 99)), ip4=random.choice(range(10, 99)))

    def getUUid(self):
        uuidStr = uuid.uuid4()
        return str(uuidStr)


    def getStartTime(self):
        return int(round(time.time() * 1000))

    def getEndTime(self):
        return int(round(time.time() * 1000))

    def getEtlPortOld(self):
        date = getEtlPort()
        if len(date) == 0:
            port = 0
            return port
        else:
            port = random.choice(date)
            return port

    def getEtlPortNew(self):
        oldNew = getEtlPort()
        count = 0
        flag = True
        while flag or count>=10:
            newPort = self.getPort()
            count = count + 1
            if newPort not in oldNew:
                flag = False
                return newPort
        return ''

    def getEtlPortIll(self):
        portList = [port for port in range(10000, 20000)]
        port = random.choice(portList)
        return port

if __name__ == '__main__':
    date = ParaDateFiledServer().getEtlPortIll()
    print(date)