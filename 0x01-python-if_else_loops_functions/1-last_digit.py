#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_diget(_number):
    last_dig = _number % 10
    if _number < 0:
        last_dig = -(10 - last_dig)
    if last_dig == -10:
        last_dig = 0
    return (last_dig)

if last_diget(number) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_diget(number)))
elif last_diget(number) == 0:
    print("Last digit of {} is {} and is 0".format(number, last_diget(number)))
elif last_diget(number) < 6 and last_diget(number) != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_diget(number)))
