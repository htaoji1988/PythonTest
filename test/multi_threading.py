import threading
import os


def scp_packages(file, user, host, destination):
    os.system('scp -r %s %s@%s:/%s' % (file, user, host, destination))

