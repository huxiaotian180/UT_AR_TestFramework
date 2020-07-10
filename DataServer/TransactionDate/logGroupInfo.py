#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 11:45
# @Author  : Evan.hu
from interface.ar_manager.LogGroup.commit.getLogGroupInfo import getAllLogGroupType, getLogGroupMapIpAndTags
import random

class LogGroup(object):

    def __init__(self):
        self.__GroupId = ''

    def getLogGroupIndex(self):
        typeGroup = {}
        dataType = getAllLogGroupType()
        if len(dataType) == 0:
            return ''

        for key in dataType.keys():
            type = dataType[key]['type']
            getIpAndTags = getLogGroupMapIpAndTags(type)
            if len(getIpAndTags[0]) > 0:
                typeGroup[key] = {}
                typeGroup[key]['name'] = dataType[key]['name']
                typeGroup[key]['type'] = dataType[key]['type']
                typeGroup[key]['ip'] = getIpAndTags[0]
                typeGroup[key]['tags'] = getIpAndTags[1]

        if len(typeGroup) == 0:
            return ''
        else:
            self.__GroupId = typeGroup
        id = random.choice(list(typeGroup.keys()))
        return id

    def logGroupHostIp(self,id):
        self.getLogGroupIndex()
        ip= self.__GroupId[id]['ip']
        return random.choice(ip)

    def logGroupHostTags(self,id):
        self.getLogGroupIndex()
        tags = self.__GroupId[id]['tags']
        if len(tags) == 0:
            return '*'
        return random.choice(tags)

    def logGroupDataType(self,id):
        self.getLogGroupIndex()
        tags = self.__GroupId[id]['type']
        return tags

    def logGroupId(self,id):
        return id


if __name__ == '__main__':
    id = '08AUATtc'
    date = LogGroup().logGroupDataType(id)
    print(date)