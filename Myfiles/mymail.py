#!/usr/bin/python
# coding=utf-8

# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText

mailto_list = ["823136165@qq.com"]
mail_host = "smtp.126.com"  # 设置服务器
mail_user = "htaoji1988"  # 用户名
mail_pass = "Ht511301"  # 口令
mail_postfix = "126.com"  # 发件dd 箱的后缀


def send_mail(to_list, sub, content):
    me = "htaoji1988@126.com"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['11111'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world!"):
        print "发送成功"
    else:
        print "发送失败"
