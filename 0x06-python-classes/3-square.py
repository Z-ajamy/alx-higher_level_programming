#!/usr/bin/python3
"""Square module for geometric shape representation with area calculation.

This module defines a Square class for representing square geometric shapes
with a private size attribute that includes validation and area calculation.
"""


class Square:
    """A class to represent a square geometric shape with area calculation.
    
    This class provides functionality to create square objects with a specified
    size that must be a non-negative integer. The size is stored as a private
    attribute and validated during initialization. The class also provides
    methods to calculate the area of the square.
    
    Attributes:
        __size (int): The private size/side length of the square (non-negative integer).
        
    Example:
        >>> square = Square(5)
        >>> square.area()
        25
    """
    
    def __init__(self, size=0):
        """Initialize a new Square instance with validation.
        
        Creates a square object with the specified size after validating that
        the size is an integer and non-negative. The size is stored as a private
        attribute (__size) to prevent direct external access.
        
        Args:
            size (int): The side length of the square. Must be a non-negative integer.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative (less than 0).
            
        Example:
            >>> square = Square(4)
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

    def area(self):
        """Calculate and return the area of the square.
        
        Computes the area of the square by multiplying the size by itself
        (side length squared).
        
        Returns:
            int: The area of the square (size * size).
            
        Example:
            >>> square = Square(4)
            >>> square.area()
            16
            >>> square = Square(0)
            >>> square.area()
            0
        """
        return self.__size * self.__size
