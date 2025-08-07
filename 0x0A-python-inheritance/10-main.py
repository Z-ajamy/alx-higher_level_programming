#!/usr/bin/python3
Square = __import__('10-square').Square

try:
    s = Square("13")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
