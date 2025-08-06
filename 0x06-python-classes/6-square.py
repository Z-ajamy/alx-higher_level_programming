#!/usr/bin/python3
"""Module for representing and manipulating geometric squares.

This module provides a Square class that allows creation and manipulation
of square objects with size and position properties, including methods
for calculating area and printing visual representations.
"""


class Square:
    """
    A class to represent a square with size and position attributes.
    
    This class provides functionality to create squares with specified
    dimensions and positions, calculate their area, and display them
    visually using ASCII characters.
    
    Attributes:
        size (int): The side length of the square.
        position (tuple): A tuple of two non-negative integers representing
                         the (x, y) position offset for printing.
    """
    
    def __init__(self, size=0, position=(0,0)):
        """
        Initialize a new Square instance.
        
        Args:
            size (int, optional): The side length of the square. Defaults to 0.
            position (tuple, optional): A tuple of two non-negative integers
                                      representing the position offset. Defaults to (0,0).
        
        Raises:
            TypeError: If size is not an integer or position is not a valid tuple.
            ValueError: If size is negative or position contains negative values.
        """
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """
        Get the size of the square.
        
        Returns:
            int: The side length of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, size=0):
        """
        Set the size of the square.
        
        Args:
            size (int, optional): The side length of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    @property
    def position(self):
        """
        Get the position of the square.
        
        Returns:
            tuple: A tuple of two non-negative integers representing the position offset.
        """
        return self.__position
    
    @position.setter
    def position(self, val=(0,0)):
        """
        Set the position of the square.
        
        Args:
            val (tuple, optional): A tuple of two non-negative integers 
                                 representing the position offset. Defaults to (0,0).
        
        Raises:
            TypeError: If val is not a tuple of exactly 2 non-negative integers.
        """
        if type(val) is tuple and len(val) == 2 and type(val[0]) is \
        int and type(val[1]) is int and val[0] >= 0 and val[1] >= 0:
            self.__position = val
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
   
    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
            int: The area of the square (size squared).
        """
        return self.size * self.size
    
    def my_print(self):
        """
        Print a visual representation of the square using '#' characters.
        
        The square is printed with vertical offset based on position[1] 
        (number of newlines) and horizontal offset based on position[0] 
        (number of spaces). If size is 0, prints an empty line.
        """
        if self.size > 0:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#"*self.size)
        else:
            print()
