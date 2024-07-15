#!/usr/bin/python3
"""
Module: square

This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square shape, inherits from Rectangle.

    Attributes:
        size (int): The size of the square (both width and height).
    """

    def __init__(self, size):
        """Initializes a Square object with a specified size.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
