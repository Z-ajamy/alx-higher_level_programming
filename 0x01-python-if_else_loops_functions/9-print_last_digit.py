#!/usr/bin/python3
def print_last_digit(number):
    i = number % 10
    if (number < 0 and (number % 10) != 0):
        i = (10 - i)

    print("{}".format(i), end='')
    return i
