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
                raise TypeError
            else:
                raise ValueError
