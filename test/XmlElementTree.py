from xml.etree import ElementTree as ET

root = ET.parse('somexml/movies')
movies = root.findall('movie')


for movie in movies:
    print(movie.find('type').text)
