#!/usr/bin/python3
'''Define a class Square.'''


class Square:
    """ Represent a square. """
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize a new Square.


        Args:
            size (int):the size of the Square must be greater or equal zero
            position (int, int)
        '''

        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

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
            print("")
        else:
            for m in range(self.position[1]):
                print()
            for i in range(self.__size):
                for n in range(self.position[0]):
                    print(" ", sep='', end='')
                for j in range(self.__size):
                    print("#", sep='', end='')
                print("")
