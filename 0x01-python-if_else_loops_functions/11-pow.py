#!/usr/bin/env python3
def pow(a, b):
    c = 1
    if b > 0:
        for i in range(0, b):
            c = c * a
    elif b < 0:
        b = b * -1
        for i in range(0, b):
            c = c * a
        c = 1/c
    return c
