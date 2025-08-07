#!/usr/bin/python3
"""Module for Square class implementation with alternative inheritance approach.

This module provides a Square class that inherits from Rectangle with
direct size validation and storage, implementing square-specific
functionality with explicit size parameter handling.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class to represent a square that inherits from Rectangle.
    
    This class implements a square by inheriting from Rectangle and
    performing explicit validation and initialization. It validates
    the size parameter directly and stores it as a private attribute
    while also initializing the parent Rectangle with equal dimensions.
    
    Attributes:
        size (int): The side length of the square (positive integer).
    
    Inherits from:
        Rectangle: Provides rectangle functionality including area calculation
                  and string representation methods.
    """
    
    def __init__(self, size):
        """
        Initialize a new Square instance with explicit size validation.
        
        Creates a square by first validating the size parameter using
        the inherited integer_validator method, then initializing the
        parent Rectangle with equal width and height, and storing the
        size as a private attribute.
        
        Args:
            size (int): The side length of the square. Must be a positive integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
