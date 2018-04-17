import requests

headers = {'Accept': 'application/x-yaml'}

payload = {'username': 'apple',
           'password': 'apple',
           'eauth': 'pam', }

session = requests.session()

r = session.get('https://172.16.107.138:8000/login', params=payload, verify=False)
print(r)
