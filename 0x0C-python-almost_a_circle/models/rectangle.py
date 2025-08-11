#!/usr/bin/python3
"""
Module for Rectangle class with automatic ID management and positioning.

This module provides a Rectangle class that inherits from Base, combining
geometric rectangle properties (width, height) with positioning coordinates
(x, y) and automatic ID management functionality.
"""

from .base import Base


class Rectangle(Base):
    """
    A class to represent a rectangle with position and automatic ID management.
    
    This class inherits from Base to gain automatic ID management functionality
    while implementing rectangle-specific properties including dimensions
    (width, height) and position coordinates (x, y). All properties are
    managed through getter and setter methods.
    
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate position of the rectangle.
        y (int): The y-coordinate position of the rectangle.
        id (int): The unique identifier inherited from Base class.
    
    Inherits from:
        Base: Provides automatic ID management functionality.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        
        Creates a rectangle with specified dimensions and optional position
        coordinates. The ID is managed through the parent Base class, either
        using a provided value or auto-generating a unique one.
        
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x (int, optional): The x-coordinate position. Defaults to 0.
            y (int, optional): The y-coordinate position. Defaults to 0.
            id (int, optional): A specific ID for the rectangle. If None,
                               an auto-generated unique ID will be assigned.
                               Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """
        Get the width of the rectangle.
        
        Returns:
            int: The width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, val):
        """
        Set the width of the rectangle with validation.
        
        Args:
            val: The new width value for the rectangle.
        
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("width"))
        elif val <= 0:
            raise ValueError ("{} must be > 0".format("width"))
        self.__width = val

    @property
    def height(self):
        """
        Get the height of the rectangle.
        
        Returns:
            int: The height of the rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, val):
        """
        Set the height of the rectangle with validation.
        
        Args:
            val: The new height value for the rectangle.
        
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("height"))
        elif val <= 0:
            raise ValueError ("{} must be > 0".format("height"))
        self.__height = val

    @property
    def x(self):
        """
        Get the x-coordinate position of the rectangle.
        
        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x
    
    @x.setter
    def x(self, val):
        """
        Set the x-coordinate position of the rectangle with validation.
        
        Args:
            val: The new x-coordinate value for the rectangle.
        
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("x"))
        elif val < 0:
            raise ValueError ("{} must be > 0".format("x"))
        self.__x = val

    @property
    def y(self):
        """
        Get the y-coordinate position of the rectangle.
        
        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y
    
    @y.setter
    def y(self, val):
        """
        Set the y-coordinate position of the rectangle with validation.
        
        Args:
            val: The new y-coordinate value for the rectangle.
        
        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format("y"))
        elif val < 0:
            raise ValueError ("{} must be > 0".format("y"))
        self.__x = val