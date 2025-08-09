#!/usr/bin/python3
"""
Module for JSON file saving utilities.

This module provides utilities for saving Python objects directly to JSON files
using the standard json library with automatic file handling.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.
    
    This function takes a JSON-serializable Python object and saves it directly
    to a file in JSON format using json.dump(). If the file doesn't exist, it
    will be created. If it exists, it will be overwritten. The file is
    automatically closed after writing due to the use of a context manager.
    
    Args:
        my_obj: A JSON-serializable Python object (dict, list, str, int,
                float, bool, None, or combinations thereof) to be saved.
        filename (str): The path to the file where the JSON data will be saved.
    
    Raises:
        TypeError: If the object contains non-JSON-serializable types
                  (e.g., custom objects, functions, sets, etc.).
        FileNotFoundError: If the directory path for the file does not exist.
        PermissionError: If there are insufficient permissions to write to
                        the file or create it in the specified location.
        IOError: If there are other I/O related errors during file operations.
    
    Example:
        >>> data = {"name": "Alice", "scores": [95, 87, 92]}
        >>> save_to_json_file(data, "student.json")
        # Creates student.json with: {"name": "Alice", "scores": [95, 87, 92]}
        
        >>> save_to_json_file([1, 2, 3, 4], "numbers.json")
        # Creates numbers.json with: [1, 2, 3, 4]
        
        >>> save_to_json_file("Hello World", "message.json")
        # Creates message.json with: "Hello World"
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)