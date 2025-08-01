#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        res = number % 10
        print("{}".format(res), end="")
    else:
        res = (number * -1) % 10
        print("{}".format(res), end="")
    return res
