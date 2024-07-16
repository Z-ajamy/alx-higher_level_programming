#!/usr/bin/python3
"""
Module: student

This module defines a Student class with attributes for first name, last name,
and age.
The class also includes a method to convert the instance attributes to a
JSON-serializable dictionary.
"""


class Student:
    """Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student object with specified first name, last name,
        and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts object attributes to a JSON-serializable dictionary.

        Args:
            attrs (list of str, optional): List of attributes to include in
                the dictionary. If None, includes all attributes.

        Returns:
            dict: A dictionary representation of the object attributes.
        """
        if attrs is None or type(attrs) is not list or attrs == [] and \
                not all(type(ele) == str for ele in attrs):
            return self.__dict__
        else:
            dict = {}
            for i in attrs:
                try:
                    dict.update({i: getattr(self, i)})
                except AttributeError:
                    continue
            return dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance using a JSON object.

        Args:
            json (dict): A dictionary representing the new attribute values.
        """
        for k, v in json.items():
            setattr(self, k, v)
