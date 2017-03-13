#!/usr/bin/pyhton
account_file = 'user.txt'
lock_file = 'lock.txt'

for i in range(3):
    username = raw_input('username:').strip()
    password = raw_input('password:').strip()
    if len(username) != 0 and len('password') != 0:
        f = file(account_file)
        login_status = False
        for line in f.readlines():
            line = line.split()
            if username == line[0] and password == line[1]:
                print 'hello welcome %s login!' % username
                login_status = True
        if login_status is True:
            break
    else:
        continue
else:
    f = file(lock_file, 'a+')
    f.write(username + '\n')
    f.close()
