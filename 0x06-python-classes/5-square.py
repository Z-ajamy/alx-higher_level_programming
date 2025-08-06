#!/usr/bin/python3
"""Square module for geometric shape representation with property access and printing.

This module defines a Square class for representing square geometric shapes
with a size property that includes validation, area calculation, and visual
printing functionality. The size attribute is accessible via property 
decorators for controlled access.
"""


class Square:
    """A class to represent a square geometric shape with property-based size access and printing.
    
    This class provides functionality to create square objects with a specified
    size that must be a non-negative integer. The size is accessible through
    a property that validates values during assignment. The class also provides
    methods to calculate the area of the square and print a visual representation.
    
    Attributes:
        __size (int): The private size/side length of the square (non-negative integer).
        
    Example:
        >>> square = Square(3)
        >>> square.size
        3
        >>> square.area()
        9
        >>> square.my_print()
        ###
        ###
        ###
    """
    
    def __init__(self, size=0):
        """Initialize a new Square instance.
        
        Creates a square object with the specified size. The size is validated
        through the size property setter during initialization.
        
        Args:
            size (int, optional): The side length of the square. Defaults to 0.
                                Must be a non-negative integer.
            
        Raises:
            TypeError: If size is not an integer (raised by size setter).
            ValueError: If size is negative (raised by size setter).
            
        Example:
            >>> square = Square(4)
            >>> square = Square()  # Uses default size of 0
        """
        self.size = size
        
    @property
    def size(self):
        """Get the size of the square.
        
        Returns the current size (side length) of the square.
        
        Returns:
            int: The size/side length of the square.
            
        Example:
            >>> square = Square(5)
            >>> square.size
            5
        """
        return self.__size

    @size.setter
    def size(self, size=0):
        """Set the size of the square with validation.
        
        Sets the size (side length) of the square after validating that the
        size is an integer and non-negative.
        
        Args:
            size (int, optional): The side length of the square. Defaults to 0.
                                Must be a non-negative integer.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative (less than 0).
            
        Example:
            >>> square = Square(5)
            >>> square.size = 10
            >>> square.size
            10
            >>> square.size = -1  # Raises ValueError
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
            >>> square.size = 3
            >>> square.area()
            9
        """
        return self.__size * self.__size

    def my_print(self):
        """Print a visual representation of the square using '#' characters.
        
        Prints the square to the console using '#' characters. Each row and
        column is represented by a '#' character. If the size is 0, nothing
        is printed (no output).
        
        Example:
            >>> square = Square(3)
            >>> square.my_print()
            ###
            ###
            ###
            >>> square = Square(0)
            >>> square.my_print()
            # No output for size 0
            >>> square = Square(1)
            >>> square.my_print()
            #
        """
        if self.size > 0:
            for i in range(self.size):
                for i in range(self.size):
                    print("#",end="")
                print()
