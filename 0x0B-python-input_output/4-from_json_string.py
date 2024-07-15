#!/usr/bin/python3
"""
Module: json_parser

This module defines a function to convert a JSON string to a Python object.
"""


def from_json_string(my_str):
    """Converts a JSON formatted string to a Python object.

    Args:
        my_str (str): The JSON formatted string to convert.

    Returns:
        any: The Python object represented by the JSON string.
    """
    import json
    return json.loads(my_str)
