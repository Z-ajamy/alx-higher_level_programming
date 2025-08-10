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
                    dict[i] = self.__dict__[i]
            return dict
        return self.__dict__
            
    def reload_from_json(self, json):
        """
        Reload student attributes from a JSON dictionary.
        
        This method updates the student instance's attributes using values
        from a provided dictionary (typically from JSON data). It only
        updates attributes that already exist in the instance, ensuring
        that the instance structure is preserved.
        
        Args:
            json (dict): A dictionary containing attribute names as keys
                        and their new values. Only keys that correspond
                        to existing instance attributes will be processed.
        
        Note:
            This method only updates existing attributes and does not add
            new attributes to the instance. Non-existent attributes in the
            json parameter are ignored.
        
        Example:
            >>> student = Student("Alice", "Johnson", 20)
            >>> student.reload_from_json({'first_name': 'Bob', 'age': 25})
            >>> print(student.first_name)  # Bob
            >>> print(student.age)         # 25
            
            >>> student.reload_from_json({'first_name': 'Carol', 'new_attr': 'ignored'})
            >>> print(student.first_name)  # Carol
            >>> # new_attr is not added to the instance
        """
        for i in json:
            if i in self.__dict__:
                setattr(self, i, json[i])
