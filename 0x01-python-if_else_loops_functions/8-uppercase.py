#!/usr/bin/python3
def uppercase(str):
    s = ''
    for i in str:
        t = i
        if (ord(t) >= 97 and ord(t) <= 122):
            t = chr(ord(t) - 32)
        s += t
    print(s)
