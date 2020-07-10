#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  @Time    : 2020/2/28 17:30
#  @Author  : Evan.hu
#  @File    : entrance
import platform

from entity import operation_logging
from entity.opertation_file import file_clear, properties
import re,os,subprocess,settings,pytest

# 初始化日志
log = operation_logging.TestLog().getlog()

def run(server='',model=''):
    # 清空历史测试报告内容
    file_clear()

    # 写入ENV环境参数
    properties()

    # 生成测试结果
    model_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'TestCases'
    run_model = model_path + os.path.sep + server + os.path.sep + model
    result_dir = settings.REPORT_RESULT
    run_cmd = ['-q', '-s', '--timeout-method=thread','--timeout=120',run_model, '--alluredir={dir}'.format(dir=result_dir)]
    pytest.main(run_cmd)

    # run_cmd = ['pytest', '-q', '-s', '--timeout=120',run_model, '--alluredir', result_dir]
    # subprocess.run(run_cmd)

    # run_cmd = ['pytest', '-q', '-s', '--timeout=120',run_model, '--alluredir', result_dir]
    # subprocess.Popen('pytest -q -s --timeout=120 {run_model} --alluredir {result_dir}'.format(run_model='C:\\UT_AR_TestFramework\\TestCases\\Demo\\DemoXiaoth',result_dir='C:\\report\\result'))


def restart():
    report_cmd = settings.REPORT_CMD

    # 生成测试结果
    os.popen(report_cmd)

    # 生成测试报告
    url_cmd = settings.URL_CMD
    os.popen(url_cmd)

def killWindows():
    # 发现服务进程
    cmd = os.popen('netstat -aon|findstr "8083"')
    result = str(cmd.read()).replace(' ', '')
    id_list = re.findall(r"LISTENING\d{1,7}", result)
    kill_id = ''
    for pid in id_list:
        kill_id = re.findall(r'\d+', pid)
        if len(kill_id) > 0:
            break

    # 杀死进程PID
    if len(kill_id) > 0:
        kill_cmd = 'taskkill /f /pid {id}'.format(id=int(kill_id[0]))
        os.popen(kill_cmd)

def killLinux():
    # 发现服务进程
    cmd = os.popen('netstat -ntlp|grep "8083"')
    result = str(cmd.read()).replace(' ', '')
    id_list = re.findall(r"LISTEN\d{1,7}", result)
    kill_id = ''
    for pid in id_list:
        kill_id = re.findall(r'\d+', pid)
        if len(kill_id) > 0:
            break

    # 杀死进程PID
    if len(kill_id) > 0:
        kill_cmd = 'kill -9 {id}'.format(id=int(kill_id[0]))
        os.popen(kill_cmd)

def stop():
    plat = platform.system()
    if plat in ['Windows', 'windows']:
        killWindows()

    elif plat in ['Linux', 'linux']:
        killLinux()

if __name__ == '__main__':
    run(server='',model='')
