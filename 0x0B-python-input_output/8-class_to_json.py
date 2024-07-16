#!/usr/bin/python3
"""
Module: class_to_json

This module provides a function to convert a class
instance's attributes to a JSON string.
"""


import json


def class_to_json(obj):
    """Converts a class instance's attributes to a JSON string.

    Args:
        obj (object): The instance of a class to convert.

    Returns:
        str: A JSON string representation of the object's
        attributes.
    """
    return json.dumps(obj.__dict__)
