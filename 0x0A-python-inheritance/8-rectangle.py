#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle shape, inherits from BaseGeometry.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes a Rectangle object with specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, new_width):
        """Sets the width of the rectangle.

        Args:
            new_width (int): The width value to set.

        Raises:
            TypeError: If new_width is not an integer.
            ValueError: If new_width is not greater than 0.
        """
        self.integer_validator("width", new_width)
        self.__width = new_width
    
    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Sets the height of the rectangle.

        Args:
            new_height (int): The height value to set.

        Raises:
            TypeError: If new_height is not an integer.
            ValueError: If new_height is not greater than 0.
        """
        self.integer_validator("height", new_height)
        self.__height = new_height
