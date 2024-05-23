#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    lenv = len(sys.argv) - 1
    res = 0
    for i in range(lenv):
        res = res + int(sys.argv[i + 1])
    print("{}".format(res))
