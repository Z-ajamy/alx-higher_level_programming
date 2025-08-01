#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        print(i, j, sep="", end="")
        if i != 9 or j != 9:
            print(" ,", end="")
else:
    print()
