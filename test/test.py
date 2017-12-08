from pymongo import MongoClient

conn = MongoClient('120.92.168.14', 27118)
db = conn.test
table = db.test_collections


def get_i():
    for i in table.find({"x": 3}):
        return i


i = get_i()
print(i)
