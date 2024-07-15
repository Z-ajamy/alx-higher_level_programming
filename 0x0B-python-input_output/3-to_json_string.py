#!/usr/bin/python3
"""
Module: json_converter

This module defines a function to convert a Python object to a JSON string.
"""


def to_json_string(my_obj):
    """Converts a Python object to a JSON formatted string.

    Args:
        my_obj (any): The Python object to convert to JSON.

    Returns:
        str: The JSON formatted string representing the Python object.
    """
    import json
    return json.dumps(my_obj)
