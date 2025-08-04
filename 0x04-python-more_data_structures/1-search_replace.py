#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        for i, j in enumerate(my_list):
            if j == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
    return new_list