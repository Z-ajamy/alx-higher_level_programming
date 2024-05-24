#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list) - 1
    if my_list[idx] < 0 and l < idx and idx < 0 :
        return None
    return(my_list[idx])
