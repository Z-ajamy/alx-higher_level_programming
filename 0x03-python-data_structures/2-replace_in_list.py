#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenth = len(my_list) - 1
    if lenth < idx or idx < 0 or my_list[idx] < 0:
        return my_list
    
    my_list[idx] = element
    return (my_list)
