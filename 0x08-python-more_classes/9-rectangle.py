#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value=0):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value=0):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2
    
    def __print__(self):
        s = ""
        if self.width > 0:
            for i in range(self.height):
                s = s + str(self.print_symbol) * self.width
                if i < self.height - 1:
                    s = s + "\n"
        return s
    
    def __str__(self):
        s = ""
        if self.width > 0:
            for i in range(self.height):
                s = s + str(self.print_symbol) * self.width
                if i < self.height - 1:
                    s = s + "\n"
        return s
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
