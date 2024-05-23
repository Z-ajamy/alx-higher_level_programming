#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    lenv = len(sys.argv) - 1

    if lenv == 0:
        print("0: argument")
    elif lenv == 1:
        print("1: argument")
    else:
        print("{}: arguments".format(lenv))

    for i in range(lenv):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
