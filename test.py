import os.path
import shutil
import logging
import zipfile
import subprocess
from datetime import datetime
import threading
from itertools import dropwhile

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s')


class ThreadClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pass


def get_date():
    return datetime.now().strftime('%Y-%m-%d_%H:%M:%S')  # 2016-03-01


def getUpgradeWar(directory, suffix=".war"):
    files = []
    for root, dir, file in os.walk(directory):
        if len(file) > 0:
            files = [x for x in file if x.endswith(suffix)]
    return files


def getStatus(abs_path):
    cmd = "ps -ef | grep {} | grep -v grep".format(abs_path)
    try:
        pid = subprocess.check_output(cmd, shell=True)
        if len(pid) > 0:
            return True
        else:
            return False

    except subprocess.CalledProcessError:
        logging.warning('not have apache tomcat process id')
    finally:
        pass


def stop_service(abs_path):
    '''
        abs_path is cataina_home path
        example /usr/local/apache-tomcat-7.0.65
        example /opt/tomcat

    '''
    grepcmd = "ps -ef | grep {} | grep -v grep".format(abs_path)

    try:
        pid = subprocess.check_output(grepcmd, shell=True).split()
        if len(pid) > 0:
            pid = subprocess.check_output(grepcmd, shell=True).split()[1:2]

            pidcode = pid[0].decode('utf-8')

            logging.info("tomcat process id is {0}, now stop service.".format(pidcode))

            killcmd = '/bin/kill -s SIGKILL ' + pidcode

            returncode = subprocess.call([killcmd], shell=True)

            return returncode

    except subprocess.CalledProcessError:
        logging.warning('not have process id')

    finally:
        pass


def startService(abs_path):
    cmd = "ps -ef | grep {} | grep -v grep".format(abs_path)

    if not getStatus(abs_path):
        logging.info("tomcat is not working now,  startup tomcat process ")

        cmd = os.path.join(abs_path, "bin", "startup.sh")

        subprocess.call([cmd], shell=True)
    else:
        logging.info("tomcat process is working now, do not need start up")


class Auto:
    def __init__(self, **kwargs):
        '''
        :param args:
        :param kwargs:
            catalina home dir
            application_name:   xsh-application-inisde or xsh-service-inside
            app_package:        xsh-application-inside.war or xsh-service-inside.war
            bak_dir
            application conf dir
            cache dir
            resource dir
        '''
        self.app_package = kwargs.get('app_package', None)
        self.src_dir = kwargs.get('src_dir', '/tmp')
        self.catalina_home = kwargs.get('catalina_home', None)

    def _getDir(self, *args):

        if self.catalina_home is None:
            return 'error'
        path = os.path.join(self.catalina_home, *args)
        return path

    def cleanCacheWork(self, *args):
        '''
            delete catalina_home/work/Catalina/localhost cache file
        '''
        path = self._getDir(*args)
        if os.path.exists(path):
            shutil.rmtree(path)

    def copyNewPackage(self, webapps='webapps'):
        if self.catalina_home is None:
            return 'error'
        src = os.path.join(self.src_dir, self.app_package)
        dst = os.path.join(self.catalina_home, webapps)
        logging.info('copy new package From {} To {}'.format(src, dst))
        shutil.copy2(src, dst)

    def _deleteOldFiles(self, *args):
        path = os.path.join(self.catalina_home, *args)
        if os.path.exists(path):
            logging.info('delete old package files {}'.format(path))
            shutil.rmtree(path)

    def backupOldPackage(self, *args):

        if self.catalina_home is None:
            return 'error'

        path = os.path.join(self.catalina_home, *args)  # application_name/bak/2016-01-01

        if not os.path.exists(path):
            os.mkdir(path)

        # delete old files
        self._deleteOldFiles('webapps', self.app_package.split('.')[0])

        src = self._getDir('webapps', self.app_package)

        if os.path.isfile(src):
            logging.info('back up old pacage war files From {} To {}'.format(src, path))
            shutil.move(src, path)

    def extraPackage(self, webapps='webapps'):

        path = os.path.join(self.catalina_home, webapps, self.app_package.split('.')[0])

        if not os.path.exists(path):
            os.mkdir(path)
        try:
            myzip = zipfile.ZipFile(self._getDir('webapps', self.app_package))
            myzip.extractall(path)
        except zipfile.BadZipFile:
            logging.error("zip file is bad")
        finally:
            myzip.close()

    def _getDirfile(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                yield os.path.join(root, file)

    def checkOnConfig(self, *args):

        '''
            check on jdbc config file
        '''

        file = os.path.join(self.catalina_home, *args)

        with open(file) as fp:
            for line in dropwhile(lambda line: line.startswith('#'), fp):
                if 'oracle' in line:
                    yield line


if __name__ == '__main__':

    if os.environ.get('CATALINA_HOME'):
        catalina_home = os.environ.get('CATALINA_HOME')
    elif os.environ.get('TOMCAT_HOME'):
        catalina_home = os.environ.get('TOMCAT_HOME')
    else:
        # catalina_home = '/Users/apple/apache-tomcat-7.0.68'
        catalina_home = '/opt/tomcat'

    date_dir = get_date()

    files = getUpgradeWar('/tmp/sales')

    stop_service(catalina_home)

    for file in files:
        app = Auto(app_package=file,
                   catalina_home=catalina_home,
                   src_dir='/tmp/sales')

        app.backupOldPackage('bak', date_dir)
        app.cleanCacheWork('work', 'Catalina')
        app.copyNewPackage()
        app.extraPackage()

    startService(catalina_home)
