#!/usr/bin/python3
"""
Module: mylist

This module defines a custom list class, MyList, which inherits from Python's
built-in list.

Classes:
    MyList(list): A custom list class that adds additional functionality
    to the standard list.
"""


class MyList(list):
    """A custom list class inheriting from Python's built-in list.

    This class adds additional functionality to the standard list:
    - print_sorted: Prints the elements of the list in sorted order.

    Methods:
        print_sorted(): Prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
