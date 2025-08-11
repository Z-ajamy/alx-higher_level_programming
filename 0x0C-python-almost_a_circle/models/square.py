#!/usr/bin/python3
"""
Module for representing and manipulating squares.

This module defines the Square class, which inherits from the Rectangle class
and represents a special case where the width and height are always equal.
It supports initialization with size, position offsets, ID management, 
size property getters/setters, and provides a formatted string representation.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, a special type of rectangle where width == height.

    Inherits from:
        Rectangle: Provides attributes and methods for geometric rectangles.

    Attributes:
        size (int): The length of each side of the square (must be > 0).
        x (int): Horizontal offset from the origin (must be >= 0).
        y (int): Vertical offset from the origin (must be >= 0).
        id (int): Unique identifier for the instance, handled by Base.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance with a given size and position.

        Args:
            size (int): The side length of the square (must be > 0).
            x (int, optional): The horizontal offset (>= 0). Defaults to 0.
            y (int, optional): The vertical offset (>= 0). Defaults to 0.
            id (int, optional): The identifier for the square. Defaults to None.

        Raises:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size <= 0, or if x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square.

        Format:
            [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: A formatted string describing the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The current side length of the square.
        """
        return self.height

    @size.setter
    def size(self, val):
        """
        Set the size of the square.

        This sets both the width and height of the square to ensure
        that it remains a true square (equal sides).

        Args:
            val (int): The new size of the square (must be > 0).

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val <= 0.
        """
        self.height = val
        self.width = val
