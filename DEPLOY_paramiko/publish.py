# coding=utf-8

import Deploy
import sys


def deploy_pre(ips, user, keypath, cmds):
    t = Deploy.Deploy()
    for ip in ips.split("|"):
        t.PublishWithKey(ip, user, keypath, cmds.split("|"))


if __name__ == '__main__':
    deploy_pre(sys.argv[1], sys.argv[2], "/home/tomcat/.ssh/id_rsa",
               sys.argv[3])
