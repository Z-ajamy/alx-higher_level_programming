#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    res = 0
    for i in range(1, num):
        res += int(argv[i])
    print(res)
    