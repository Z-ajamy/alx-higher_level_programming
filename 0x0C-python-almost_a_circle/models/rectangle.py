#!/usr/bin/python3
"""
Module for representing and manipulating rectangles.

This module provides the Rectangle class, which inherits from the Base class
and allows the creation and manipulation of rectangle objects. The class
supports setting dimensions and positions with validation, calculating area,
displaying a text-based representation, updating attributes dynamically,
and providing a formatted string representation.

Classes:
    Rectangle: Represents a geometric rectangle with width, height, and (x, y) position.
"""

from .base import Base


class Rectangle(Base):
    """
    Represents a rectangle with width, height, and position coordinates.

    Inherits from:
        Base: The parent class providing ID management.

    Attributes:
        width (int): The width of the rectangle (must be > 0).
        height (int): The height of the rectangle (must be > 0).
        x (int): The horizontal offset of the rectangle (must be >= 0).
        y (int): The vertical offset of the rectangle (must be >= 0).
        id (int): Identifier for the instance, managed by the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance with the given dimensions and position.

        Args:
            width (int): The width of the rectangle (must be > 0).
            height (int): The height of the rectangle (must be > 0).
            x (int, optional): The horizontal offset (must be >= 0). Defaults to 0.
            y (int, optional): The vertical offset (must be >= 0). Defaults to 0.
            id (int, optional): The identifier for the rectangle. Defaults to None.

        Raises:
            TypeError: If any provided argument is not an integer.
            ValueError: If width or height <= 0, or if x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Set the width of the rectangle.

        Args:
            val (int): The new width (must be > 0).

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val <= 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("width"))
        elif val <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = val

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Set the height of the rectangle.

        Args:
            val (int): The new height (must be > 0).

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val <= 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("height"))
        elif val <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = val

    @property
    def x(self):
        """
        Get the horizontal offset of the rectangle.

        Returns:
            int: The current horizontal offset.
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Set the horizontal offset of the rectangle.

        Args:
            val (int): The new horizontal offset (must be >= 0).

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val < 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("x"))
        elif val < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = val

    @property
    def y(self):
        """
        Get the vertical offset of the rectangle.

        Returns:
            int: The current vertical offset.
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Set the vertical offset of the rectangle.

        Args:
            val (int): The new vertical offset (must be >= 0).

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val < 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("y"))
        elif val < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = val

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area, calculated as width * height.
        """
        return self.height * self.width

    def display(self):
        """
        Print a text-based representation of the rectangle.

        The rectangle is represented by the '#' character, with vertical
        and horizontal offsets determined by y and x respectively.
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a formatted string representation of the rectangle.

        Format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            str: The formatted string.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update attributes of the rectangle.

        This method can accept positional arguments (*args) or keyword
        arguments (**kwargs). The order of positional arguments is:
        id, width, height, x, y.

        Args:
            *args: Variable length positional arguments.
                0: id
                1: width
                2: height
                3: x
                4: y
            **kwargs: Arbitrary keyword arguments matching attribute names.

        Example:
            r.update(10, 20, 30, 5, 5)
            r.update(id=10, width=20, height=30, x=5, y=5)
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        elif kwargs:
            for i in kwargs:
                if hasattr(self, i):
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle.

        Returns:
            dict: A dictionary with keys 'id', 'width', 'height', 'x', and 'y'.
        """
        dic = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
        return dic