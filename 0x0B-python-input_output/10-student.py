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
    
    def to_json(self, attrs=None):
        """
        Convert the student instance to a JSON-serializable dictionary.
        
        This method returns instance attributes as a dictionary that can be
        easily serialized to JSON format. It supports selective attribute
        retrieval when a list of attribute names is provided, or returns
        all attributes when no filter is specified.
        
        Args:
            attrs (list, optional): A list of attribute names to include
                                   in the returned dictionary. If None or
                                   not a list, all attributes are returned.
                                   Only existing attributes will be included.
        
        Returns:
            dict: A dictionary containing the requested instance attributes
                  as key-value pairs. If attrs is provided and is a list,
                  only attributes present in both the attrs list and the
                  instance's __dict__ will be included. Otherwise, all
                  instance attributes are returned.
        
        Example:
            >>> student = Student("Alice", "Johnson", 20)
            >>> student.to_json()
            {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 20}
            
            >>> student.to_json(['first_name', 'age'])
            {'first_name': 'Alice', 'age': 20}
            
            >>> student.to_json(['first_name', 'nonexistent'])
            {'first_name': 'Alice'}
            
            >>> student.to_json("not_a_list")
            {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 20}
        """
        if isinstance(attrs, list):
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = getattr(self, i)
            return dic
        return self.__dict__