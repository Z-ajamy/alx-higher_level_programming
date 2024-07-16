#!/usr/bin/python3
"""
Module: json_file_loader

This module defines a function to load JSON data from a file into a Python
object.
"""


def load_from_json_file(filename):
    """Loads JSON data from a file into a Python object.

    Args:
        filename (str): The name of the file containing JSON data.

    Returns:
        any: The Python object parsed from the JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the JSON data in the file is invalid.

    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
