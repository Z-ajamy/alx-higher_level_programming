#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    count = 0
    for i in my_list:
        if i == search:
            new_list.append(replace)
            continue
        new_list.append(i)

    return (new_list)
