import requests

url = "http://httpbin.org/"
url_ip = url + "ip"
url_get = url + "get"

r1 = requests.get(url_ip)

#print(r1.headers)

params = {
    'params1': "hello",
    'params2': "world!"
}
r2 = requests.get(url_get, params=params)
print(r2.text)
