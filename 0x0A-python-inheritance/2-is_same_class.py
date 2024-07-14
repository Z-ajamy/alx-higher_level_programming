#!/usr/bin/python3
"""
Module: is_same_class

This module defines a function to check if an object is exactly
an instance of a specified class.

Functions:
    is_same_class(obj, a_class): Checks if obj is exactly
    an instance of a_class.
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
