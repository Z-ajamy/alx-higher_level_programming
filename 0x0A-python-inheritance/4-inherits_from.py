#!/usr/bin/python3
"""
Module: inherits_from

This module defines a function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

Functions:
    inherits_from(obj, a_class): Checks if obj is an instance of a class that inherited from a_class.
"""

def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the inheritance of obj against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
