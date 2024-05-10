#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    stat = "positive"
elif number < 0:
    stat = "negative"
else:
    stat = "zero"

print("{} is {}".format(number, stat))
