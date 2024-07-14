#!/usr/bin/python3
"""
Module: is_kind_of_class

This module defines a function to check if an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.

Functions:
    is_kind_of_class(obj, a_class): Checks if obj is an instance of,
    or if the object is an instance of a class that inherited from, a_class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
