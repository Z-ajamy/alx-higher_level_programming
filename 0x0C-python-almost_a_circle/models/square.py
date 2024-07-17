#!/usr/bin/python3
"""
Module: square

This module defines a Square class that inherits from the Rectangle class.

The Square class includes attributes for size, x, and y coordinates, and
    an ID inherited from the Rectangle class.
It also includes property methods for attribute validation and a string
    representation method.

Classes:
    Square: Represents a square shape.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape, inherits from Rectangle.

    Attributes:
        size (int): The size of the square (both width and height).
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square object with specified size, x and y
            coordinates, and optional ID.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square. Defaults to 0.
            y (int): The y-coordinate of the square. Defaults to 0.
            id (int or None): ID to assign to the object. If None, assigns
                a new incremented value of __nb_objects from Base class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: Gets or sets the size of the square."""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the size of the square.

        Args:
            size (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.width = size
        self.height = size

    def __str__(self):
        """Returns a string representation of the Square object.

        Returns:
            str: The string representation of the Square object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)
