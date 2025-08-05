#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for n in range(x):
            print("{}".format(my_list[n]), end="")
            i = i + 1
        print()
        return i
    except IndexError:
        print()
        return i
