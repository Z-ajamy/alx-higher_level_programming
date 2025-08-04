#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_1 = sorted(a_dictionary)
    for i in list_1:
        print("{}: {}".format(i, a_dictionary[i]))