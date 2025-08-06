#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, val=(0,0)):
        if type(val) is tuple and len(val) == 2 and type(val[0]) is \
        int and type(val[1]) is int and val[0] >= 0 and val[1] >= 0:
            self.__position = val
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    
    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size > 0:
            print("\n" * self.position[1], end="")

            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#"*self.size)
        else:
            print()
    
