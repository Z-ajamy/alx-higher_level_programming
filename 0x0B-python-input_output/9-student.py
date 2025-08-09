#!/usr/bin/python3
"""
Module for Student class representation and JSON serialization.

This module provides a Student class that represents student information
with basic attributes and includes functionality for JSON serialization
of the student data.
"""


class Student:
    """
    A class to represent a student with basic information.
    
    This class stores student information including first name, last name,
    and age. It provides functionality to convert the student instance to
    a JSON-serializable dictionary format.
    
    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        
        Creates a student with the specified first name, last name, and age.
        All parameters are stored as instance attributes.
        
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        Convert the student instance to a JSON-serializable dictionary.
        
        This method returns all instance attributes as a dictionary that
        can be easily serialized to JSON format. It provides a convenient
        way to export student data for storage or transmission.
        
        Returns:
            dict: A dictionary containing all instance attributes as key-value
                  pairs, where keys are attribute names and values are the
                  corresponding attribute values.
        
        Example:
            >>> student = Student("Alice", "Johnson", 20)
            >>> student.to_json()
            {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 20}
        """
        return self.__dict__