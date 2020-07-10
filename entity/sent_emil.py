#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @Time    : 2020/2/28 16:20
#  @Author  : Evan.hu
#  @File    : sent_emil

import smtplib
import datetime

class SendEmail:
    def send_mail(self):
        i = datetime.datetime.now()
        timeNow = "{day}/{month}/{year} {hour}:{minute}".format(day=i.day, month=i.month, year=i.year, hour=i.hour,
                                                                minute=i.minute)
        HOST = 'smtp.163.com'
        # 配置服务的端口，默认的邮件端口是25.
        PORT = '25'
        # 3> 指定发件人和收件人。
        FROM = 'gy1360562@163.com'
        TO = 'Evan.hu@aishu.cn'
        # 邮件标题
        SUBJECT = 'Anyrobot自动化测试报告({time})'.format(time=timeNow)
        CONTENT = 'Anyrobot测试成功,详细bug情况请查看AT测试报告'

        # 创建邮件发送对象
        smtp_obj = smtplib.SMTP()

        # 数据在传输过程中会被加密。
        # smtp_obj = smtplib.SMTP_SSL()

        # 需要进行发件人的认证，授权。
        # smtp_obj就是一个第三方客户端对象
        smtp_obj.connect(host=HOST, port=PORT)

        # 如果使用第三方客户端登录，要求使用授权码，不能使用真实密码，防止密码泄露。
        res = smtp_obj.login(user=FROM, password='**********')
        print('登录结果：', res)

        # 发送邮件
        msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'Subject: {}'.format(SUBJECT), '', CONTENT])
        print(msg)
        smtp_obj.sendmail(from_addr=FROM, to_addrs=TO, msg=msg.encode('utf-8'))