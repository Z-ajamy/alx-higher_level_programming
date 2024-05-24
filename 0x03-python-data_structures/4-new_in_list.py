#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return (None)
    length = len(my_list)
    if idx < 0:
        return (None)
    new_list = []
    for i in range(length):
        if i == idx:
            new_list.append(element)
            continue
        new_list.append(my_list[i])
    return (new_list)
