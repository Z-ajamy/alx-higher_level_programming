#!/usr/bin/python3
"""
Module for defining a Rectangle class.

This module provides a Rectangle class that defines width and height attributes,
and includes methods for calculating area, perimeter, and string representations.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.

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
            value (int, optional): New width of the rectangle. Defaults to 0.

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
            value (int, optional): New height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either width or height is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __print__(self):
        """
        Create a string representation of the rectangle using '#' characters.

        Returns:
            str: The rectangle drawn as '#' characters, line by line.
        """
        s = ""
        if self.width > 0:
            for i in range(self.height):
                s = s + "#" * self.width
                if i < self.height - 1:
                    s = s + "\n"
        return s

    def __str__(self):
        """
        Return the informal string representation of the rectangle.

        Returns:
            str: String representation using '#' characters.
        """
        s = ""
        if self.width > 0:
            for i in range(self.height):
                s = s + "#" * self.width
                if i < self.height - 1:
                    s = s + "\n"
        return s

    def __repr__(self):
        """
        Return the official string representation of the rectangle.

        Returns:
            str: String in the format 'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Print a message upon deletion of the rectangle instance.
        """
        print("Bye rectangle...")
