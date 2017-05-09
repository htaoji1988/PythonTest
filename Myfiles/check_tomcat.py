#!/usr/bin/python
# coding=utf-8

import os
import urllib
import commands
import time
import socket

# 声明JAVA环境变量
# JAVA_HOME = "/usr/java/jdk1.7.0_79/"
# 定义时间变量
date_now = time.strftime('%Y-%mymail.py-%d %H:%M:%S', time.localtime(time.time()))
# 定义启动脚本路径
StartTomcat = "sh /apps/service/tomcat/bin/startup.sh"
# 定义测试URL
WebUrl = "http://127.0.0.1:8099/kafka/"
# 获取进程ID
process_id = commands.getoutput("ps -ef|grep /apps/service/tomcat/|grep -v grep|awk '{print $2}'")

# 设置URL超时时间
socket.setdefaulttimeout(5)


def restart_tomcat(pid):  # 定义重启方法
    pid = int(pid)
    try:
        print date_now, "reboot-tomcat:"
        os.kill(pid, 9)
        time.sleep(5)
        print "开始执行startup.sh"
        os.system(StartTomcat)
    except IOError, e:
        print e


def check_tomcat():  # 定义检查tomcat方法
    print "----------------------------"
    print date_now, "开始检查 tomcat..."
    if process_id:  # 如果存在进程ID则往下执行
        print "进程已存在，检测url是否能访问..."
        try:
            response_code = urllib.urlopen(WebUrl).getcode()
            if response_code == 200:
                print "URL访问正常无需重启tomcat..."
            else:
                restart_tomcat(process_id)
        except IOError:
            restart_tomcat(process_id)
    else:
        print "进程不存在,开始执行startup.sh"
        os.system("JAVA_HOME=/usr/java/jdk1.7.0_79")
        os.system(StartTomcat)


if __name__ == "__main__":
    check_tomcat()
