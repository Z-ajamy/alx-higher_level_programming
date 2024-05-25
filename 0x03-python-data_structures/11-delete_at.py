#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None or not my_list:
        return None
    length = len(my_list)
    if idx >= length or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
