#!/usr/local/pyenv/shims/python3.5

import json
import urllib.request
import socket
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s] [%(name)s] (%(levelname)s) %(message)s',
)


class ZabbixAPIException(Exception):
    """
        generic zabbix api exception
    code list:
        - 32602 - invalid params
        - 32500 - no permissions
    """
    pass


class Zabbix_API:
    HEADER = {"Content-Type": "application/json",
              "User-Agent": "python/zabbix_api"}

    URL = 'http://172.20.3.11/zabbix'

    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.header = self.HEADER
        self.url = url + '/api_jsonrpc.php'
        self.ipaddr = self.__get_local_ip()
        self.id = 0
        self.authID = None
        self.__status = True  # default host is monitored, enable,

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def __get_local_ip(self):
        ''' get local host ipaddr, return a list '''
        return [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if
                not ip.startswith("127.")][:1]

    def do_request(self, method, auth=None, filter=None, **kwargs):
        request_json = {
            "jsonrpc": "2.0",
            "method": method,
            "params": kwargs or {},
            "id": self.id,
        }
        if auth:
            request_json.update({'auth': self.authID})
        if filter:
            request_json['params'].update(filter)
        req = urllib.request.Request(self.url,
                                     json.dumps(request_json).encode('utf-8'))

        for key, value in self.header.items():
            req.add_header(key, value)
        try:
            results = urllib.request.urlopen(req)
        except urllib.request.URLError as e:
            logging.info(
                'url error, method is : {}, message is {}'.format(method, e))
            raise ZabbixAPIException("urllib url error %s" % e)
        except socket.timeout:
            logging.info('timeout error, method is: {}'.format(method))
            raise ZabbixAPIException("HTTP read timeout", )

        else:
            response = json.loads(results.read().decode('utf-8'))
            results.close()
            print(response)
            return response['result']

    def user_login(self, method="user.login", **kwargs):
        '''
            ret is user auth id.
        '''

        ret = self.do_request(method, **{'user': self.username,
                                         'password': self.password})
        return ret

    def host_id(self, hostip, method="host.get", **kwargs):
        ''' return hostid to update operation'''
        self.id = 1
        ret = self.do_request(method, auth=self.authID,
                              filter={"filter": {"host": hostip}}, **kwargs)
        return ret[0]['hostid']

    def host_update(self, method="host.update", **kwargs):
        self.id = 1
        hostid = self.host_id(self.ipaddr, **{'output': 'extend'})
        if self.status:  # monitored
            self.do_request(method, auth=self.authID,
                            **{'hostid': hostid, 'status': 1})
            self.status = False
        else:  # not monitored
            self.do_request(method, auth=self.authID,
                            **{'hostid': hostid, 'status': 0})
            self.status = True


if __name__ == '__main__':
    zabbix = Zabbix_API('xxxxxxx', 'xxxxxxx', url=Zabbix_API.URL)
    zabbix.authID = zabbix.user_login()
    zabbix.status = False
    zabbix.host_update()

    # do jenkins update step by step
    # ............

    zabbix.status = True
    zabbix.host_update()
