#!/usr/bin/python3
"""Square module for geometric shape representation.

This module defines a Square class for representing square geometric shapes
with a private size attribute.
"""


class Square:
    """A class to represent a square geometric shape.
    
    This class provides functionality to create square objects with a specified
    size. The size is stored as a private attribute to encapsulate the data.
    
    Attributes:
        __size (int or float): The private size/side length of the square.
        
    Example:
        >>> square = Square(5)
        >>> isinstance(square, Square)
        True
    """
    
    def __init__(self, size):
        """Initialize a new Square instance.
        
        Creates a square object with the specified size. The size is stored
        as a private attribute (__size) to prevent direct external access.
        
        Args:
            size (int or float): The side length of the square.
            
        Example:
            >>> square = Square(4)
            >>> square._Square__size  # Access private attribute (not recommended)
            4
        """
        self.__size = size
