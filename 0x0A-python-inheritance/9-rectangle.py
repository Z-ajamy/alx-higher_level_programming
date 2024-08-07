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

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A formatted string showing the width and
            height of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
