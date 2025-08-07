#!/usr/bin/python3
"""
Module for representing and manipulating geometric rectangles.

This module provides a Rectangle class that allows creation and manipulation
of rectangle objects with width and height properties, including validation
to ensure proper dimensions.
"""


class Rectangle:
    """
    A class to represent a rectangle with width and height attributes.
    
    This class provides functionality to create rectangles with specified
    dimensions and includes property validation to ensure non-negative
    integer values for width and height.
    
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        
        Returns:
            int: The width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value=0):
        """
        Set the width of the rectangle.
        
        Args:
            value (int, optional): The width of the rectangle. Defaults to 0.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        
        Returns:
            int: The height of the rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, value=0):
        """
        Set the height of the rectangle.
        
        Args:
            value (int, optional): The height of the rectangle. Defaults to 0.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
