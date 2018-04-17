# coding=utf-8
import pexpect
import paramiko
import os
import sys


class Deploy:
    def __init__(self):
        pass

    # 使用密码执行
    def PublishWithPasswd(self, hosts, user, passwd, cmds):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for host in hosts:
            print("connecting")
            client.connect(hostname=host, username=user, password=passwd)
            print("connected")
            for command in cmds:
                stdin, stdout, stderr = client.exec_command(command)
                print(stdout.read())
        client.close()

    # 使用ssh-key执行
    def PublishWithKey(self, hosts, user, keypath, cmds):
        key = paramiko.RSAKey.from_private_key_file(keypath)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for host in hosts:
            print("connecting")
            client.connect(hostname=host, username=user, pkey=key)
            print("connected")
            for command in cmds:
                stdin, stdout, stderr = client.exec_command(command)
                print(stdout.read())
        client.close()

    def scp_packages(self, file, user, host, destination):
        os.system('scp -r %s %s@%s:/%s' % (file, user, host, destination))

    def scp_password(self, file, user, passwd, host, destination):
        if os.path.isdir(file):
            cmdline = 'scp -r %s %s@%s:%s' % (file, user, host, destination)
        else:
            cmdline = 'scp %s %s@%s:%s' % (file, user, host, destination)
        try:
            child = pexpect.spawn(cmdline)
            child.expect('password:')
            child.sendline(passwd)
            child.expect(pexpect.EOF)
            # child.interact()
            # child.read()
            # child.expect('$')
            print("uploading")
        except:
            print("upload faild!")


if __name__ == "__main__":

    publish = Deploy()

    if sys.argv[1] == "MPART-SERVER_TEST":
        servers = [
            "172.26.132.59",
            #"172.16.107.136",
        ]

        commonds = [
            "/home/admin/shell/publish.sh",
            #"ls",
        ]

        publish.PublishWithKey(servers, 'admin', "/home/tomcat/.ssh/id_rsa", commonds)
    else:
        print("wrong parameter!")
        exit()
