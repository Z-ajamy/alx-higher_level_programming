#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        s = set(my_list)
        res = 0
        for i in s:
            res = res + i
        return res
