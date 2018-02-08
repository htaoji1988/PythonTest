from urllib import request
from bs4 import BeautifulSoup


content = request.urlopen('http://www.baidu.com')
soup = BeautifulSoup(content, 'html.parser')

print(soup.p['class'])
