#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that inherits from the Base class.

The Rectangle class includes attributes for width, height, x, and y
coordinates,
and an ID inherited from the Base class. It also includes property methods for
attribute validation.

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
                newincremented value of __nb_objects from Base class.
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
        """
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
        """
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
        """
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
        """
        self.__y = y
