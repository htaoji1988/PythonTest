#!/usr/bin/python
# coding=utf-8

import os
import shutil
import subprocess
from datetime import datetime
import time

package_name = 'jenkins.war'  # jar包名
new_package = '/tmp/src/' + package_name  # 新包路径
tomcat_home = '/Users/tt/test/usr/tomcat7/'  # tomcat目录
webapp_home = tomcat_home + 'webapps/'  # 工程目录
date_now = datetime.now().strftime('%Y%m%d_%H%M%S')  # 当前时间
backup_path = '/Users/tt/test/bak/' + str(date_now)  # 备份目录
logfile = tomcat_home + 'logs/catalina.out'


def get_pid():
    try:
        pid = subprocess.check_output('ps -ef|grep ' + tomcat_home + ' |grep -v grep', shell=True).split()[1:2]
        return pid[0].decode('utf-8')

    except Exception as e:
        print(str(e))


def back_up():
    os.mkdir(backup_path)
    print('开始备份...')
    try:
        shutil.copy(webapp_home + package_name, backup_path)
        print('完成备份...')
    except Exception as e:
        print('备份失败:' + str(e))
        exit()


def stop_service(pid):
    if pid:
        try:
            print('停止tomcat服务...')
            os.system('kill -9 ' + pid)
            time.sleep(5)
        except Exception as e:
            print(str(e))
    else:
        print('tomcat进程未启动无需停止...')


def start_service():
    try:
        print('开始启动tomcat...')
        os.system(tomcat_home + 'bin/startup.sh')
        time.sleep(10)
    except Exception as e:
        print(e)


def copy_newpackage(src_path, dis_tpath):
    if not os.path.exists(src_path):
        print("没有发现新的war包，请检查!")
        exit()
    else:
        if os.path.exists(webapp_home):
            shutil.rmtree(webapp_home)
            os.mkdir(webapp_home)
        else:
            os.mkdir(webapp_home)
        shutil.copy(src_path, dis_tpath)
        print('已将war包拷贝到webapps目录')


def deploy_logs():
    os.system('tail -30 ' + logfile)


if __name__ == "__main__":
    stop_service(get_pid())
    back_up()
    copy_newpackage(new_package, webapp_home)
    start_service()
    deploy_logs()
