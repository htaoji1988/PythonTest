#!/usr/bin/python
import urllib.request
import json
import re

url = 'http://172.21.222.111/zabbix/api_jsonrpc.php'

login_info = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "admin",
        "password": "tt_test",
        # "userData": "true"
    },
    "id": 1,
}


# 登陆
def login(url, values):
    data = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data, {'Content-Type': 'application/json-rpc'})
    response = urllib.request.urlopen(req, data, timeout=5)
    a = response.read().decode(encoding='utf-8')
    output = json.loads(a)
    try:
        message = output['result']
    except:
        message = output['error']['data']
        print(message)
        quit()

    return output['result']


# 获取主机IP
def gethost(auth_code):
    method = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 2,
        "auth": auth_code
    }
    get_host_data = json.dumps(method).encode('utf-8')
    req = urllib.request.Request(url, get_host_data, {'Content-Type': 'application/json-rpc'})
    result = urllib.request.urlopen(req, get_host_data, timeout=5)
    response = json.loads(result.read())
    result.close()
    return response


if __name__ == '__main__':
    a = gethost(login(url, login_info))
    print(a)
