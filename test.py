import paramiko

ssh = paramiko.SSHClient()
ssh.connect('172.16.107.137', username='root', password='admin')
ssh.exec_command("touch >/tmp/test.txt")