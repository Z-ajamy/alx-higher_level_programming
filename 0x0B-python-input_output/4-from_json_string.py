#!/usr/bin/python3
"""
Module for JSON deserialization utilities.

This module provides utilities for converting JSON string representations
back to Python objects using the standard json library.
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.
    
    This function takes a JSON-formatted string and converts it back to
    the corresponding Python object using the json.loads() method. The
    JSON string must be valid and properly formatted.
    
    Args:
        my_str (str): A valid JSON-formatted string to be converted to
                     a Python object.
    
    Returns:
        object: The Python object represented by the JSON string. The type
                depends on the JSON content (dict for objects, list for arrays,
                str for strings, int/float for numbers, bool for booleans,
                None for null).
    
    Raises:
        json.JSONDecodeError: If the input string is not valid JSON or
                             contains syntax errors.
        TypeError: If the input is not a string.
    
    Example:
        >>> from_json_string('{"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}
        
        >>> from_json_string('[1, 2, 3, "hello"]')
        [1, 2, 3, 'hello']
        
        >>> from_json_string('"simple string"')
        'simple string'
        
        >>> from_json_string('null')
        None
        
        >>> from_json_string('42')
        42
        
        >>> from_json_string('true')
        True
    """
    return json.loads(my_str)