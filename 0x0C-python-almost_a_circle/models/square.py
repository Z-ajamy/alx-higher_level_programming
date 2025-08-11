#!/usr/bin/python3
"""
Module for representing and manipulating squares.

This module provides the Square class, which inherits from the Rectangle class
and represents a square with equal width and height. It supports initialization
with position, ID management (inherited from Base), and provides a formatted
string representation.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle where width == height.

    Inherits from:
        Rectangle: Provides attributes and methods for geometric rectangles.

    Attributes:
        size (int): The length of each side of the square (must be > 0).
        x (int): The horizontal offset of the square (must be >= 0).
        y (int): The vertical offset of the square (must be >= 0).
        id (int): Identifier for the instance, managed by the Base class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance with a given size and position.

        Args:
            size (int): The size of the square's sides (must be > 0).
            x (int, optional): The horizontal offset (must be >= 0). Defaults to 0.
            y (int, optional): The vertical offset (must be >= 0). Defaults to 0.
            id (int, optional): The identifier for the square. Defaults to None.

        Raises:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size <= 0, or if x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a formatted string representation of the square.

        Format:
            [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: The formatted string.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )
