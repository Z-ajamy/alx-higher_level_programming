#!/usr/bin/python3
"""Square module for geometric shape representation with validation.

This module defines a Square class for representing square geometric shapes
with a private size attribute that includes type and value validation.
"""


class Square:
    """A class to represent a square geometric shape with validation.
    
    This class provides functionality to create square objects with a specified
    size that must be a non-negative integer. The size is stored as a private
    attribute and validated during initialization.
    
    Attributes:
        __size (int): The private size/side length of the square (non-negative integer).
        
    Example:
        >>> square = Square(5)
        >>> isinstance(square, Square)
        True
        >>> square = Square()  # Default size is 0
        >>> isinstance(square, Square)
        True
    """
    
    def __init__(self, size=0):
        """Initialize a new Square instance with validation.
        
        Creates a square object with the specified size after validating that
        the size is an integer and non-negative. The size is stored as a private
        attribute (__size) to prevent direct external access.
        
        Args:
            size (int, optional): The side length of the square. Defaults to 0.
                                Must be a non-negative integer.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative (less than 0).
            
        Example:
            >>> square = Square(4)
            >>> square = Square()  # Uses default size of 0
            >>> square = Square(-1)  # Raises ValueError
            Traceback (most recent call last):
                ...
            ValueError: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size