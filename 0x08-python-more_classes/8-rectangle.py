#!/usr/bin/python3
"""A module for representing a Rectangle object.

This module includes a class that defines a rectangle with
width and height attributes, methods to calculate its area and perimeter,
and class attributes to keep track of the number of instances.
"""


class Rectangle:
    """Represents a rectangle shape.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (str): The symbol used for string representation.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with specified width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either
            the width or height is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two Rectangle instances.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance
            of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string depicting the rectangle using the `print_symbol`.
        """
        result = []

        if self.height == 0 or self.width == 0:
            return ''

        for i in range(self.height):
            for j in range(self.width):
                result.append(str(self.print_symbol))
            if i < self.height - 1:
                result.append('\n')
        return "".join(result)

    def __repr__(self):
        """Returns a string representation of the Rectangle object.

        Returns:
            str: A formatted string showing the width
            and height of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when a Rectangle object is deleted.

        This method is called when the garbage collector destroys the object.
        It prints "Bye rectangle..." to indicate that the Rectangle object
        has been deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
