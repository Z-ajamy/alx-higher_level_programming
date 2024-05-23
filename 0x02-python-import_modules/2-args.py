#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    lenv = len(sys.argv)

    if lenv == 1:
        print("0: argument")
    else:
        print("{}: arguments".format(lenv - 1))

    for i in range(lenv - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
