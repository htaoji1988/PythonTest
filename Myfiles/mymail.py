#! /usr/bin/python
# coding:utf-8
'''
[INFORMATION]
Zabbix Send Email With Python
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

from email.mime.text import MIMEText
import smtplib
import sys


def send_mail(_to_email, _subject, _message):
    # 定义邮件发送
    smtp_host = 'smtp.126.com'
    from_email = 'htaoji1988@126.com'
    passwd = 'Ht511301'
    msg = MIMEText(_message, 'plain', 'utf-8')
    msg['Subject'] = _subject
    smtp_server = smtplib.SMTP(smtp_host, 25)
    smtp_server.login(from_email, passwd)
    smtp_server.sendmail(from_email, [_to_email], msg.as_string())
    smtp_server.quit()


if __name__ == '__main__':
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
