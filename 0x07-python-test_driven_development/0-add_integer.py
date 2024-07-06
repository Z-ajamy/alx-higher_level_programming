#!/usr/bin/python3
"""
    Add module
"""


def add_integer(a, b=98):
    """
        Add functhion that add two numbers and return the result.

        Args:

            a (int or float) :the first number
            b (int or float) :the second number

        Returns:

            int : the product of a + b
        """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
