#!/usr/bin/python3
"""
Module for converting class instances to JSON-serializable dictionaries.

This module provides utilities for extracting the attributes of class instances
into dictionary format that can be easily serialized to JSON.
"""


def class_to_json(obj):
    """
    Convert a class instance to a JSON-serializable dictionary.
    
    This function returns the __dict__ attribute of a class instance, which
    contains all the instance's attributes as key-value pairs. The resulting
    dictionary can be used for JSON serialization if all attribute values
    are JSON-serializable types.
    
    Args:
        obj: A class instance object whose attributes will be extracted.
    
    Returns:
        dict: A dictionary containing all instance attributes as key-value
              pairs, where keys are attribute names (strings) and values
              are the corresponding attribute values.
    
    Note:
        This function only returns instance attributes stored in __dict__.
        It does not include class attributes, methods, or properties.
        The returned dictionary is only JSON-serializable if all attribute
        values are JSON-serializable types (str, int, float, bool, None,
        list, dict with JSON-serializable contents).
    
    Example:
        >>> class Student:
        ...     def __init__(self, name, age, grades):
        ...         self.name = name
        ...         self.age = age
        ...         self.grades = grades
        
        >>> student = Student("Alice", 20, [85, 90, 78])
        >>> class_to_json(student)
        {'name': 'Alice', 'age': 20, 'grades': [85, 90, 78]}
        
        >>> class Person:
        ...     def __init__(self, name):
        ...         self.name = name
        ...         self.active = True
        
        >>> person = Person("Bob")
        >>> class_to_json(person)
        {'name': 'Bob', 'active': True}
    """
    return obj.__dict__