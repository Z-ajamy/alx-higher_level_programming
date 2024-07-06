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

        Can hendel integral and float numbers, but it tearn
        the float to integral.
            >>> add_integer(1, 2)
            3
            >>> add_integer(0, 0)
            0
            >>> add_integer(-1, 2)
            1
            >>> add_integer(-1, -1)
            2
            >>> add_integer(1, 4645452434454324231)
            4645452434454324232
            >>> add_integer(5.8, 1.2)
            6

        It make type error if a or b was not integral or float.
        >>> add_integer("1", 2)
        Traceback(most recent call last):
            ...
        ValueError: a must be an integer
        >>> add_integer(1, "2")
        Traceback(most recent call last):
            ...
        ValueError: b must be an integer

        Handel 0 args.
        >>> add_integer()
        98
        """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
