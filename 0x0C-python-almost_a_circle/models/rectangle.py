#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that inherits from the Base class.

The Rectangle class includes attributes for width, height, x, and y
    coordinates,
and an ID inherited from the Base class. It also includes property methods
    for attribute validation.

Classes:
    Rectangle: Represents a rectangle shape.
"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle shape, inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle object with specified width, height,
        x and y coordinates, and optional ID.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle. Defaults to 0.
            y (int): The y-coordinate of the rectangle. Defaults to 0.
            id (int or None): ID to assign to the object. If None, assigns a
                new incremented value of __nb_objects from Base class.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle.

        Args:
            width (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is not greater than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle.

        Args:
            height (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is not greater than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """int: Gets or sets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle.

        Args:
            x (int): The x-coordinate value to set.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """int: Gets or sets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle.

        Args:
            y (int): The y-coordinate value to set.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle using the '#' character."""
        for i in range(self.height):
            for n in range(self.width):
                print("#", end='')
            if i < self.height:
                print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id,
                    self.x,
                    self.y,
                    self.width,
                    self.height)
