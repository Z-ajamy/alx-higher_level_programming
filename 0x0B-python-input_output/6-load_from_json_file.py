#!/usr/bin/python3
"""
Module for JSON file loading utilities.

This module provides utilities for loading and parsing JSON files directly
into Python objects using the standard json library with automatic file handling.
"""

import json


def load_from_json_file(filename):
    """
    Load and parse a JSON file into a Python object.
    
    This function opens a JSON file, reads its contents, and converts the
    JSON data back to the corresponding Python object using json.load().
    The file is automatically closed after reading due to the use of a
    context manager (with statement).
    
    Args:
        filename (str): The path to the JSON file to be loaded and parsed.
    
    Returns:
        object: The Python object represented by the JSON file content.
                The type depends on the JSON structure (dict for objects,
                list for arrays, str for strings, int/float for numbers,
                bool for booleans, None for null).
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON or
                             syntax errors.
        PermissionError: If there are insufficient permissions to read the file.
        IOError: If there are other I/O related errors during file operations.
        UnicodeDecodeError: If the file contains characters that cannot be
                           decoded using the default encoding.
    
    Example:
        >>> load_from_json_file("student.json")
        {'name': 'Alice', 'scores': [95, 87, 92]}
        
        >>> load_from_json_file("numbers.json")
        [1, 2, 3, 4]
        
        >>> load_from_json_file("message.json")
        'Hello World'
        
        >>> load_from_json_file("config.json")
        {'debug': True, 'version': 1.2, 'features': None}
    """
    
    with open(filename, 'r') as f:
        return json.load(f)