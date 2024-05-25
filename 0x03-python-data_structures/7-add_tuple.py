#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_b = len(tuple_b)
    if len_b < 2:
        b = 0
    else:
        b = tuple_a[1]
    if len_b == 0:
        a = 0
        b = 0
    else:
        a = tuple_b[0]
        b = tuple_a[1]
    res_tuple = (tuple_a[0] + a, tuple_a[1] + b)
    return res_tuple
