#!/usr/bin/python3
"""Module for class type comparison utilities.

This module provides utilities for comparing object types and determining
exact class matches between objects and class types.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.
    
    This function performs an exact type comparison between an object
    and a class, returning True only if the object's type matches
    the specified class exactly. It does not consider inheritance -
    subclasses will return False.
    
    Args:
        obj: Any Python object to check.
        a_class: A class type to compare against.
    
    Returns:
        bool: True if the object is exactly an instance of the specified
              class, False otherwise (including for subclasses).
    
    Example:
        >>> is_same_class(1, int)
        True
        
        >>> is_same_class("hello", str)
        True
        
        >>> is_same_class([1, 2, 3], list)
        True
        
        >>> class MyList(list):
        ...     pass
        >>> my_list = MyList()
        >>> is_same_class(my_list, list)
        False
        >>> is_same_class(my_list, MyList)
        True
    """
    return type(obj) == a_class
