# coding=utf-8

import paramiko
import os

tomcat_home = '/apps/usr/tomcat7'
hosts = "172.16.107.137"
cmd = ['touch /tmp/666']


# 定义发布方法
def deploy(user, host):
    k = paramiko.RSAKey.from_private_key_file("/Users/tt/.ssh/id_rsa")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("connecting")
    c.connect(hostname=host, username=user, pkey=k)
    print("connected")
    # 开始killtomcat进程

    commands = cmd
    for command in commands:
        stdin, stdout, stderr = c.exec_command(command)
        print(stdout.read())
    c.close()


deploy('root', hosts)
