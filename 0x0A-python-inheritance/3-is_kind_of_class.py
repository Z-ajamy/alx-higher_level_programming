#!/usr/bin/python3
"""
Module for inheritance-aware class checking utilities.

This module provides utilities for checking if an object is an instance
of a specified class or any of its subclasses, supporting inheritance
hierarchies.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclasses.
    
    This function performs an inheritance-aware type check, returning True
    if the object is an instance of the specified class or any class that
    inherits from it. This is different from exact type matching as it
    considers the entire inheritance hierarchy.
    
    Args:
        obj: Any Python object to check.
        a_class: A class type to compare against.
    
    Returns:
        bool: True if the object is an instance of the specified class
              or any of its subclasses, False otherwise.
    
    Example:
        >>> is_kind_of_class(1, int)
        True
        
        >>> is_kind_of_class("hello", str)
        True
        
        >>> class MyList(list):
        ...     pass
        >>> my_list = MyList()
        >>> is_kind_of_class(my_list, list)
        True
        >>> is_kind_of_class(my_list, MyList)
        True
        
        >>> is_kind_of_class(42, object)
        True
        
        >>> is_kind_of_class("text", int)
        False
    """
    return isinstance(obj, a_class)
