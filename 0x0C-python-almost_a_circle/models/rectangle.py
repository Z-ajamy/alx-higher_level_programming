#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that inherits from the Base class.

The Rectangle class includes attributes for width, height, x, and y coordinates
and an ID inherited from the Base class. It also includes property methods for
attribute validation, an area method to calculate the area of the rectangle,
a display method to print the rectangle using the '#' character, and a static
method __the_shape to create a string representation of a rectangle shape.

Classes:
    Rectangle: Represents a rectangle shape.
"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle shape, inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle object with specified width, height,
        x and y coordinates, and optional ID.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle. Defaults to 0.
            y (int): The y-coordinate of the rectangle. Defaults to 0.
            id (int or None): ID to assign to the object. If None, assigns a
                new incremented value of __nb_objects from Base class.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle.

        Args:
            width (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is not greater than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle.

        Args:
            height (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is not greater than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """int: Gets or sets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle.

        Args:
            x (int): The x-coordinate value to set.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """int: Gets or sets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle.

        Args:
            y (int): The y-coordinate value to set.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    @staticmethod
    def __the_shape(height, width):
        """Static method to create a string representation of a rectangle shape.

        Args:
            height (int): The height of the rectangle.
            width (int): The width of the rectangle.

        Returns:
            str: The string representation of the rectangle shape.
        """
        shape = ''
        for i in range(height):
            for n in range(width):
                shape += "#"
            if i < height - 1:
                shape += '\n'
        return shape

    def display(self):
        """Prints the rectangle using the '#' character."""
        shape = ''
        for y in range(self.y):
            shape += '\n'
        for i in range(self.height):
            shape += ' ' * self.x
            for n in range(self.width):
                shape += "#"
            if i < self.height - 1:
                shape += '\n'
        print(shape)

    def __str__(self):
        """Returns a string representation of the Rectangle object.

        Returns:
            str: The string representation of the Rectangle object.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id,
                    self.x,
                    self.y,
                    self.width,
                    self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle object.

        Args:
            *args: Variable length argument list.
                - If one argument is passed, it updates the id attribute.
                - If two arguments are passed, it updates the id and width attributes.
                - If three arguments are passed, it updates the id, width, and height attributes.
                - If four arguments are passed, it updates the id, width, height, and x attributes.
                - If five arguments are passed, it updates all attributes: id, width, height, x, and y.
            **kwargs: Arbitrary keyword arguments to update specific attributes.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
