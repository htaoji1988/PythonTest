import requests

headers = {'Accept': 'application/x-yaml'}

payload = {'username': 'apple',
           'password': 'apple',
           'eauth': 'pam', }

session = requests.session()

r = session.get('https://172.22.222.112:8000/login', params=payload, verify=False)
print(r)
