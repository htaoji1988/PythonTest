def generater_test(n):
    arr = [0, 1]
    while len(arr) < n:
        arr.append(arr[-1] + arr[-2])
    return arr


def yield_test(n):

    for i in range(n):
        yield i * i


for i in yield_test(101):
    print(i)
