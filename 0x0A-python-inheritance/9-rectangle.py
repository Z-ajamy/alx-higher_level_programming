#!/usr/bin/python3
"""
Module for Rectangle class implementation using BaseGeometry.

This module provides a Rectangle class that inherits from BaseGeometry
and implements rectangle-specific functionality with proper validation
of width and height parameters.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle that inherits from BaseGeometry.
    
    This class implements a rectangle with width and height attributes,
    inheriting validation functionality from BaseGeometry. It ensures
    that width and height are positive integers through the parent
    class's integer_validator method.
    
    Attributes:
        width (int): The width of the rectangle (positive integer).
        height (int): The height of the rectangle (positive integer).
    
    Inherits from:
        BaseGeometry: Provides integer validation and area method interface.
    """
    
    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        
        Creates a rectangle with the specified width and height after
        validating that both parameters are positive integers using
        the inherited integer_validator method.
        
        Args:
            width (int): The width of the rectangle. Must be a positive integer.
            height (int): The height of the rectangle. Must be a positive integer.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        This method implements the abstract area method from BaseGeometry
        to calculate the area of the rectangle using width * height.
        
        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height
    
    def __print__(self):
        """
        Return a string representation for printing purposes.
        
        This method provides a formatted string representation of the
        rectangle showing its width and height in the format
        "[Rectangle] width/height".
        
        Returns:
            str: A formatted string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def __str__(self):
        """
        Return the string representation of the rectangle.
        
        This method defines how the rectangle object is represented
        as a string when using str() or print() functions. It shows
        the width and height in the format "[Rectangle] width/height".
        
        Returns:
            str: A formatted string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
