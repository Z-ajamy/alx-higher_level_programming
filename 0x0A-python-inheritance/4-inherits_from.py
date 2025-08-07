#!/usr/bin/python3
"""
Module for inheritance relationship checking utilities.

This module provides utilities for determining if an object inherits from
a specified class without being an exact instance of that class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class but is not an exact instance.
    
    This function determines if an object is a subclass instance of the specified
    class. It returns True only if the object is an instance of a class that
    inherits from the specified class, but is not an exact instance of that class.
    
    Args:
        obj: Any Python object to check.
        a_class: A class type to check inheritance from.
    
    Returns:
        bool: True if the object inherits from the specified class but is not
              an exact instance of it, False otherwise.
    
    Example:
        >>> class Animal:
        ...     pass
        >>> class Dog(Animal):
        ...     pass
        >>> dog = Dog()
        >>> animal = Animal()
        
        >>> inherits_from(dog, Animal)
        True
        
        >>> inherits_from(animal, Animal)
        False
        
        >>> inherits_from(dog, Dog)
        False
        
        >>> inherits_from("hello", str)
        False
        
        >>> class MyList(list):
        ...     pass
        >>> my_list = MyList()
        >>> inherits_from(my_list, list)
        True
    """
    return isinstance(obj, a_class) and type(obj) != a_class
