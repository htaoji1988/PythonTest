mylist = [1, 2, 3, 4, [1, 3, 4, [6, 6, 6]]]


def print_list(the_list):
    for i in the_list:
        if isinstance(i, list):
            print_list(i)
        else:
            print i


print_list(mylist)
