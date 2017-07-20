# coding=utf-8
import pexpect
import paramiko
import os


class Deploy:
    def __init__(self):
        pass

    def PublishWithPasswd(self, host, user, passwd, cmds):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        client.connect(hostname=host, username=user, password=passwd)
        print("connected")
        commands = cmds
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read())
        client.close()

    def PublishWithKey(self, host, user, keypath, cmds):
        key = paramiko.RSAKey.from_private_key_file(keypath)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        client.connect(hostname=host, username=user, pkey=key)
        print("connected")
        commands = cmds
        for command in commands:
            print(command)
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
            print "uploading"
        except:
            print "upload faild!"
