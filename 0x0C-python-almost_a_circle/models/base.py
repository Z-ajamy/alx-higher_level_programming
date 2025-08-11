#!/usr/bin/python3
import json
"""
Module for Base class with automatic ID management and JSON serialization.

This module defines the `Base` class, which serves as the foundation for
other classes by providing:

1. **Automatic ID assignment** — Instances are given unique IDs if none are
   provided explicitly.
2. **Basic JSON serialization** — Conversion of dictionaries into JSON strings
   for storage or transmission.

Classes:
    Base: A base class with automatic ID management and static JSON serialization method.
"""

class Base:
    """
    A foundational class providing automatic ID management and JSON serialization.

    The `Base` class is designed to be inherited by other classes that require
    unique IDs and a mechanism to serialize data into JSON format. If no ID is
    provided during instantiation, it generates one automatically by incrementing
    a shared class counter.

    Attributes:
        id (int): The unique identifier for the instance.

    Class Attributes:
        __nb_objects (int): Private counter tracking the number of instances
            created without explicitly provided IDs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new `Base` instance with ID assignment logic.

        If an `id` is provided, it is assigned directly to the instance.
        If `id` is omitted or `None`, the class automatically assigns
        the next available unique ID based on an internal counter.

        Args:
            id (int, optional): A specific ID for the instance. Defaults to `None`.
                - If provided, it is assigned directly and does not affect the counter.
                - If omitted, a unique auto-incremented ID is assigned.

        Examples:
            >>> b1 = Base()
            >>> b1.id
            1

            >>> b2 = Base()
            >>> b2.id
            2

            >>> b3 = Base(99)
            >>> b3.id
            99

            >>> b4 = Base()
            >>> b4.id
            3
        """
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
