# -*- coding:utf-8 -*-

from entity.operation_sys import sysProperty
import os,sys

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

# 根据系统平台来获取属性
sysPlat = sysProperty()

# 测试报告路径
REPORT_URL = sysPlat.getReportUrl()
REPORT_RESULT = sysPlat.getReportResult()
LOG_PATH = sysPlat.getLogPath()

# 运行测试报告命令,allure
REPORT_CMD = r"allure generate {result} -o {report} --clean".format(result=REPORT_RESULT,report=REPORT_URL)
URL_CMD = r"allure open -h 0.0.0.0 -p 8083 {report}".format(report=REPORT_URL)

# 全局数据
date = {}

# AT运行模式,值为on(正式环境运行)或者off(本地环境运行)
runFlag = 'off'