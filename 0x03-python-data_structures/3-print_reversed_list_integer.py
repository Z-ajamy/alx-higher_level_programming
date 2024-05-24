#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    n = length - 1
    for i in range(length):
        print("{}".format(my_list[i + n]))
        n -= 2

'''
OR

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    n = 0
    for i in range(1, length + 1):
        print("{}".format(my_list[-i]))
        '''
