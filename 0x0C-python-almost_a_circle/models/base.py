#!/usr/bin/python3
"""Base class module for object management with JSON serialization support.

This module provides a base class that handles automatic ID assignment and
JSON serialization functionality for derived classes.
"""

import json


class Base:
    """Base class for all objects with automatic ID assignment and JSON utilities.
    
    This class provides basic functionality for object identification and JSON
    serialization. It automatically assigns unique IDs to instances and provides
    static methods for JSON string conversion.
    
    Attributes:
        __nb_objects (int): Class variable tracking the total number of objects created.
        id (int): Unique identifier for each instance.
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an ID.
        
        Creates a new Base instance with either a provided ID or an automatically
        generated unique ID. If no ID is provided, assigns the next available ID
        and increments the object counter.
        
        Args:
            id (int, optional): The ID to assign to this instance. If None,
                automatically generates the next available ID. Defaults to None.
        """
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string representation.
        
        Takes a list of dictionary objects and converts them to a JSON string.
        Handles None and empty list cases by returning an empty JSON array string.
        
        Args:
            list_dictionaries (list): A list of dictionary objects to convert to JSON.
                Can be None or an empty list.
        
        Returns:
            str: A JSON string representation of the input list. Returns "[]" if
                the input is None or an empty list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        res = json.dumps(list_dictionaries)
        return res

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.
        
        Converts a list of objects to their dictionary representations and saves
        them as JSON to a file. The filename is based on the class name with
        a .json extension.
        
        Args:
            list_objs (list): A list of objects that have a to_dictionary method.
                Can be None or an empty list, in which case an empty JSON array
                is written to the file.
        """
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs:
                list_1 = []
                for i in list_objs:
                    list_1.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(list_1))
            else:
                f.write(cls.to_json_string([]))

    @staticmethod     
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.
        
        Takes a JSON string representation and converts it back to a Python
        list of dictionaries. This is the inverse operation of to_json_string.
        
        Args:
            json_string (str): A valid JSON string to be converted to a list
                of dictionaries.
        
        Returns:
            list: A list of dictionaries parsed from the JSON string.
        
        Raises:
            json.JSONDecodeError: If the input string is not valid JSON.
        """ 
        return json.loads(json_string)
