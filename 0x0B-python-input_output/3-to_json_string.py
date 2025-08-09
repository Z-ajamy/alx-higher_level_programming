#!/usr/bin/python3
"""
Module for JSON serialization utilities.

This module provides utilities for converting Python objects to their
JSON string representations using the standard json library.
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON string representation.
    
    This function takes a Python object and converts it to a JSON-formatted
    string using the json.dumps() method. The object must be JSON serializable
    (i.e., contain only basic Python types like dict, list, str, int, float,
    bool, and None).
    
    Args:
        my_obj: A JSON-serializable Python object (dict, list, str, int, 
                float, bool, None, or combinations thereof).
    
    Returns:
        str: A JSON-formatted string representation of the input object.
    
    Raises:
        TypeError: If the object contains non-JSON-serializable types
                  (e.g., custom objects, functions, sets, etc.).
    
    Example:
        >>> to_json_string({"name": "John", "age": 30})
        '{"name": "John", "age": 30}'
        
        >>> to_json_string([1, 2, 3, "hello"])
        '[1, 2, 3, "hello"]'
        
        >>> to_json_string("simple string")
        '"simple string"'
        
        >>> to_json_string(None)
        'null'
        
        >>> to_json_string(42)
        '42'
    """
    return json.dumps(my_obj)