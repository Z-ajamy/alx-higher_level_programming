#!/usr/bin/python3
def element_at(my_list, idx):
    lenth = len(my_list) - 1
    if lenth < idx or idx < 0 or my_list[idx] < 0:
        return None
    return (my_list[idx])
