from urllib import request


content = request.urlopen('http://www.baidu.com/')
data = content.read().decode('UTF-8')
print(content.info())
