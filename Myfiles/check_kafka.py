#!/usr/bin/python
# coding=utf-8

import os
import commands
import time

# 定义时间变量
date_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 定义kafka路径
home_kafka = '/home/apps/kafka/'
kafka_bin = home_kafka + 'bin'
kafka_cfg = home_kafka + 'config/server.properties &'

# 获取进程ID
process_id = commands.getoutput("ps -ef|grep /home/apps/kafka/bin|grep -v grep|awk '{print $2}'")


def restart_kafka(kafkabin, kafkacfg):  # 定义启动方法
    try:
        print date_now, "start-kafka:"
        os.system('cd ' + kafkabin)
        os.system('nohup kafka-server-start.sh ' + kafkacfg)
    except IOError, e:
        print e


def check_kafka():  # 定义检查tomcat方法
    print "----------------------------"
    print date_now, "开始检查 kafka......"
    if process_id:  # 如果存在进程ID则往下执行
        print "进程已存在."
    else:
        print "进程不存在,开始启动."
        restart_kafka(kafka_bin, kafka_cfg)


if __name__ == "__main__":
    check_kafka()
