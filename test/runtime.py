import time


def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        func(*args, **args2)
        runtime = time.time() - t0
        return "%.3fs" % runtime

    return newFunc


@exeTime
def test1():
    a = 1
    return a


name = test1()
print(name)
