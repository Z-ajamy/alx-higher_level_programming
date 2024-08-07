#!/usr/bin/python3
"""A module for representing a Rectangle object.

This module includes a class that defines a rectangle with
width and height attributes,
and methods to calculate its area and perimeter.
"""


class Rectangle:
    """Represents a rectangle shape.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with specified width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string depicting the rectangle using '#' symbols.
        """
        result = ''

        if self.height == 0 or self.width == 0:
            return result

        for i in range(self.height):
            for j in range(self.width):
                result += '#'
            if i < self.height - 1:
                result += '\n'
        return result

    def __repr__(self):
        """Returns a string representation of the Rectangle object.

        Returns:
            str: A formatted string showing the width and height of the
            rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
