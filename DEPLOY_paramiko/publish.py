# coding=utf-8

import Deploy
import sys


def deploy_withkey(ips, user, keypath, cmds):
    t = Deploy.Deploy()
    for ip in ips.split("|"):
        ip = ip.strip()
        t.PublishWithKey(ip, user, keypath, cmds.split("|"))


def deploy_withpasswd(ips, usr, passwd, cmds):
    t = Deploy.Deploy()
    for ip in ips.split("|"):
        ip = ip.strip()
        t.PublishWithPasswd(ip, usr, passwd, cmds.split("|"))


if __name__ == "__main__":
    if sys.argv[1] == "IDM_PRE":
        server = "172.20.6.150|172.20.6.151"
        commond = "/home/admin/shell/deploy_tomcat.py"
        deploy_withkey(server, 'admin', "/home/tomcat/.ssh/id_rsa", commond)
    elif sys.argv[1] == "IDM_PRD":
        server = "172.20.2.17|172.20.2.18"
        commond = "/home/admin/shell/deploy_tomcat.py"
        deploy_withpasswd(server, 'admin', 'Hao0550', commond)
    else:
        print("bad parameter!")
