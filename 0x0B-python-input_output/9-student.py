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

    def to_json(self):
        """Converts the Student instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return self.__dict__
