import requests
import json
from requests import exceptions
from requests import Request, Session

# github的API url https://developer.github.com/

url = "http://httpbin.org/"
url_ip = url + "ip"
url_get = url + "get"
url_githubapi = "https://api.github.com"

'''
r1 = requests.get(url_ip)

print(r1.headers)

params = {
    'params1': "hello",
    'params2': "world!"
}
r2 = requests.get(url_get, params=params)
print(r2.text)
'''


def build_uri(endpoint):
    return "/".join([url_githubapi, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def reqeust_method():
    response = requests.get(build_uri("users/htaoji1988"))
    return response


def params_reqeuet():
    response = requests.get(build_uri("users"), params={"since": 11})
    return response


def json_request():
    content = ['htaoji1988@gmail.com']
    try:
        response = requests.post(build_uri("user/emails"), auth=("htaoji1988", "q13770866821"), json=content)
        return response
    except exceptions.Timeout as e:
        print(e)
        exit(code=0)


def hart_request():
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'), auth=("htaoji1988", "q13770866821"), headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)
    resp = s.send(prepped, timeout=5)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)


if __name__ == "__main__":
    hart_request()
