import time


def timeslong(func):
    def call():
        start = time.clock()
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)

    return call


@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y


print(f())
