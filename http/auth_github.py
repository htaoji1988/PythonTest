import requests

r = requests.get('https://api.github.com/user', auth=('htaoji1988', 'q13770866821'))
print(r.url)
