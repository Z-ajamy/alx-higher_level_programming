#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        exit()
    str = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        str = str + i
    print(str)
    return (str)
