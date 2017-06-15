import os


def scp(self, packages, user, hostname, dictionary):
    os.system('scp %s %s@%s:/%s' % (packages, user, hostname, dictionary))

