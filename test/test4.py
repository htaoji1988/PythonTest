def gen():
    yield "hello"
    yield "world!"


r = gen()
for i in r:
    print(i)
