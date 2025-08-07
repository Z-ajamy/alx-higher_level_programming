#!/usr/bin/python3
"""
Module for representing and manipulating rectangles.

This module defines a Rectangle class that allows for the creation and manipulation
of rectangle objects, including calculation of area, perimeter, and string 
representation using ASCII characters.
"""


class Rectangle:
    """
    A class to represent a rectangle with width and height.

    This class supports retrieving and updating dimensions with validation,
    computing area and perimeter, and producing a visual representation.

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
            value (int): The new width value.

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
            value (int): The new height value.

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
            int: The area (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)), or 0 if either dimension is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __print__(self):
        """
        Generate a string representation of the rectangle using '#' characters.

        Returns:
            str: The string representation of the rectangle, or an empty string if the dimensions are 0.
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
        Return the official string representation of the rectangle.

        Returns:
            str: A string made up of '#' characters forming the rectangle shape, or an empty string if the dimensions are 0.
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
        Return a formal string representation of the rectangle object.

        The format of the string is: 'Rectangle(width, height)', where width and height are the rectangle's dimensions.

        Returns:
            str: The string representation of the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
