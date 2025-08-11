#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

try:
    Rectangle(12, 13, -12)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "x must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(12, 13, -89)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "x must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(12, 13, -1)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "x must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(12, 13, 0)
    print("OK", end="")
except Exception as e:
    print("0 is valid for x: [{}] {}".format(type(e), e))
    exit(1)