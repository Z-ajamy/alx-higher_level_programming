#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        str = ""
        for i in my_string:
            if i == "C" or i == "c":
                continue
            str = str + i
        return str
    return None
