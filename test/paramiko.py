#!/Users/tt/anaconda/bin/python
# coding=utf-8

import paramiko

cmd = 'touch /tmp/66666'
private_key = paramiko.RSAKey.from_private_key_file('/Users/tt/.ssh/id_rsa')
t = paramiko.SSHClient()
t.set_missing_host_key_policy(paramiko.AutoAddPolicy())
t.connect(hostname='172.16.107.137', username='root', pkey=private_key)
t.exec_command(cmd)
