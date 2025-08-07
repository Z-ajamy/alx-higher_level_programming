#!/usr/bin/python3
"""
Module for object attribute inspection utilities.

This module provides utilities for inspecting Python objects and retrieving
information about their attributes and methods.
"""


def lookup(obj):
    """
    Get a list of valid attributes for an object.
    
    This function returns a list of all valid attributes and methods
    available for the given object, including both built-in and
    user-defined attributes.
    
    Args:
        obj: Any Python object to inspect.
    
    Returns:
        list: A list of strings representing all valid attribute names
              for the given object, sorted alphabetically.
    
    Example:
        >>> lookup([1, 2, 3])
        ['append', 'clear', 'copy', 'count', 'extend', ...]
        
        >>> lookup("hello")
        ['capitalize', 'casefold', 'center', 'count', 'encode', ...]
    """
    return dir(obj)
