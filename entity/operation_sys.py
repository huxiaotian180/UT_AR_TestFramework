#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 9:02
# @Author  : Evan.hu

import platform


class sysProperty(object):
    def __init__(self):
        self.__ReportUrl = ''
        self.__ReportResult = ''
        self.__LogPath = ''

    def getReportUrl(self):
        plat = platform.system()
        if plat in ['Windows', 'windows']:
            self.__ReportUrl = r"C:\report\report"

        elif plat in ['Linux', 'linux']:
            self.__ReportUrl = "/tmp/ut/report/report"

        return self.__ReportUrl

    def getReportResult(self):
        plat = platform.system()
        if plat in ['Windows', 'windows']:
            self.__ReportResult = r"C:\report\result"

        elif plat in ['Linux', 'linux']:
            self.__ReportResult = "/tmp/ut/report/result"

        return self.__ReportResult

    def getLogPath(self):
        plat = platform.system()
        if plat in ['Windows', 'windows']:
            self.__LogPath = r"C:\report\log"

        elif plat in ['Linux', 'linux']:
            self.__LogPath = '/tmp/ut/log'

        return self.__LogPath


if __name__ == '__main__':
    sys = sysProperty()
    path = sys.getReportResult()
    print(path)
