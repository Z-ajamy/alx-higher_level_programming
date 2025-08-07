#!/usr/bin/python3
"""Module for defining a Rectangle class.

This module allows the creation and manipulation of rectangles.
It supports calculating area, perimeter, and provides string representations.
It also includes functionality to compare rectangles by area.
"""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        number_of_instances (int): The number of Rectangle instances currently active.
        print_symbol (any): The symbol used when printing the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
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
            ValueError: If value is less than 0.
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
            int: The current height of the rectangle.
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
            ValueError: If value is less than 0.
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
            int: The perimeter, or 0 if width or height is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __print__(self):
        """
        Return a string representation of the rectangle using `print_symbol`.

        Returns:
            str: The rectangle represented with the print symbol.
        """
        s = ""
        if self.width > 0:
            for i in range(self.height):
                s = s + str(self.print_symbol) * self.width
                if i < self.height - 1:
                    s = s + "\n"
        return s

    def __str__(self):
        """
        Return the informal string representation of the rectangle.

        Returns:
            str: The rectangle made of print_symbol characters.
        """
        s = ""
        if self.width > 0:
            for i in range(self.height):
                s = s + str(self.print_symbol) * self.width
                if i < self.height - 1:
                    s = s + "\n"
        return s

    def __repr__(self):
        """
        Return a string representation that can recreate the object.

        Returns:
            str: A string like Rectangle(width, height).
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor for Rectangle instance.

        Decrements the instance counter and prints a message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
