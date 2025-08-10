#!/usr/bin/python3
"""
Module for Base class with automatic ID management.

This module provides a Base class that serves as a foundation for other classes
with automatic ID assignment functionality. It maintains a class-level counter
to ensure unique IDs are assigned when no specific ID is provided.
"""


class Base:
    """
    A base class with automatic ID management functionality.
    
    This class provides automatic ID assignment for instances. When an ID
    is not explicitly provided, it automatically assigns a unique ID based
    on an internal counter. The counter is shared across all instances of
    the class, ensuring unique IDs.
    
    Attributes:
        id (int): The instance ID. Either provided explicitly or auto-assigned.
    
    Class Attributes:
        __nb_objects (int): Private class attribute that tracks the number
                           of objects created with auto-assigned IDs.
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initialize a new Base instance with ID management.
        
        Creates a Base instance with either a provided ID or an automatically
        assigned unique ID. If no ID is provided, the instance receives an
        ID based on the current object counter, and the counter is incremented.
        
        Args:
            id (int, optional): A specific ID to assign to the instance.
                               If None, an auto-generated unique ID will be used.
                               Defaults to None.
        
        Note:
            When id is provided (truthy), it is used directly without affecting
            the internal counter. When id is None or falsy, a new unique ID
            is generated and the internal counter is incremented.
        
        Example:
            >>> obj1 = Base()
            >>> print(obj1.id)  # 1
            
            >>> obj2 = Base()
            >>> print(obj2.id)  # 2
            
            >>> obj3 = Base(10)
            >>> print(obj3.id)  # 10
            
            >>> obj4 = Base()
            >>> print(obj4.id)  # 3 (counter continues from where it left off)
        """
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1