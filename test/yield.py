def test(max):
    for i in range(max):
        yield i ** 2


for item in test(5):
    print item
