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

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        if isinstance(x, int) and x >= 0:
            self.__size = x
        elif not isinstance(x, int):
            raise TypeError("size must be an integer")
        elif x < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''
        prints the square.
        '''
        if self.__size == 0:
            print("\n")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", sep='', end='')
                print("")
