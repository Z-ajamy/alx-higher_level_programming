#!/usr/bin/python3
"""
Module for Square class implementation using Rectangle inheritance.

This module provides a Square class that inherits from Rectangle
and implements square-specific functionality by treating a square
as a special case of rectangle with equal width and height.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class to represent a square that inherits from Rectangle.
    
    This class implements a square by inheriting from Rectangle and
    treating it as a special case where width and height are equal.
    It leverages the Rectangle's validation and functionality while
    simplifying the interface to require only a single size parameter.
    
    Attributes:
        size (int): The side length of the square (positive integer).
                   Internally stored as both width and height in the parent Rectangle.
    
    Inherits from:
        Rectangle: Provides width/height validation, area calculation, and string representation.
    """
    
    def __init__(self, size):
        """
        Initialize a new Square instance.
        
        Creates a square with the specified size by calling the Rectangle
        constructor with size as both width and height. The size parameter
        is validated through Rectangle's inherited integer_validator method.
        
        Args:
            size (int): The side length of the square. Must be a positive integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        
        self.integer_validator("size", size)
        Rectangle.integer_validator("size", size)

