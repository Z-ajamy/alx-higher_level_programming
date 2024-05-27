#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        key_sort_dict = sorted(a_dictionary)
        for i in key_sort_dict:
            print(i, a_dictionary[i], sep=": ")
