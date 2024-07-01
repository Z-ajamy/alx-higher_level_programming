#!/usr/bin/python3
'''Define a class Square.'''


class Square:
    """ Represent a square. """
    def __init__(self, size=0):
        '''
        Initialize a new Square.


        Args:
            size (int):the size of the Square must be greater or equal zero
        '''

        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        '''
        return (self.__size * self.__size)
