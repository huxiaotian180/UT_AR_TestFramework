#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/3/3 14:03
#  @Author  : Evan.hu
#  @File    : operation_url

from urllib.parse import urljoin
from configuration.configYaml import configManage


def url(path):
    return urljoin('http://{ip}:{port}'.format(ip=configManage().getIp, port=configManage().getPort), path)