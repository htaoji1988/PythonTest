# coding=utf-8

import Deploy
import sys


def deploy_withkey(ips, user, keypath, cmds):
    t = Deploy.Deploy()
    t.PublishWithKey(ips, user, keypath, cmds)


def deploy_withpasswd(ips, usr, passwd, cmds):
    t = Deploy.Deploy()
    t.PublishWithPasswd(ips, usr, passwd, cmds)


if __name__ == "__main__":
    if sys.argv[1] == "IDM_PRE":
        servers = [
            "172.20.6.150",
            "172.20.6.151",
        ]
        commonds = [
            "/home/admin/shell/deploy_tomcat.py",
        ]
        deploy_withkey(servers, 'admin', "/home/tomcat/.ssh/id_rsa", commonds)

    elif sys.argv[1] == "IDM_PRD":
        servers = [
            "172.20.2.17",
            "172.20.2.18",
        ]
        commonds = [
            "/home/admin/shell/deploy_tomcat.py",
        ]
        deploy_withpasswd(servers, 'admin', 'Hao0550', commonds)
    else:
        print("bad parameter!")
