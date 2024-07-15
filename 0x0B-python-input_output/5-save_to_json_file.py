#!/usr/bin/python3
"""
Module: json_file_writer

This module defines a function to save a Python object as JSON in a file.
"""


def save_to_json_file(my_obj, filename):
    """Saves a Python object as JSON in a file.

    Args:
        my_obj (any): The Python object to save as JSON.
        filename (str): The name of the file to save the JSON data.

    Raises:
        IOError: If there is an error writing to the file.

    """
    import json

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
