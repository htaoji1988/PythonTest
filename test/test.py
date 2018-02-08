def my_sum(*args):
    return sum(args)


def my_average(*args):
    return sum(args) / len(args)


def dec(func):
    def in_dec(*args):
        print('in dec args=', args)
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return func(*args)

    return in_dec


my_sum = dec(my_sum)

print(my_sum(1, 2, 3, 4, 5))
print(my_average(1, 2, 3, 4, 5))

# print(my_average())
