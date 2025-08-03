#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        str1 = ""
        for i in my_string:
            if i == "C" or i == "c":
                continue
            str1 = str1 + i
        return str1
    return None
