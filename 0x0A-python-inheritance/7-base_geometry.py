#!/usr/bin/python3
"""
Module for base geometry classes and utilities.

This module provides base classes for geometric shapes and related
functionality. It serves as a foundation for implementing various
geometric objects and operations.
"""


class BaseGeometry:
    """
    A base class for geometric shapes and operations.
    
    This class serves as a foundation for implementing geometric objects
    and provides a common interface for geometric operations. It defines
    abstract methods that must be implemented by subclasses.
    """
    
    def area(self):
        """
        Calculate the area of the geometric shape.
        
        This method must be implemented by subclasses to provide
        area calculation functionality for specific geometric shapes.
        
        Returns:
            float: The area of the geometric shape.
        
        Raises:
            Exception: Always raised as this method is not implemented
                      in the base class and must be overridden by subclasses.
        """
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.
        
        This method validates that a given value is an integer and is
        greater than 0. It's used to validate geometric parameters
        such as dimensions that must be positive integers.
        
        Args:
            name (str): The name of the parameter being validated,
                       used in error messages for clarity.
            value: The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        
        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 5)  # No exception
            >>> bg.integer_validator("height", -1)
            ValueError: height must be greater than 0
            >>> bg.integer_validator("size", "5")
            TypeError: size must be an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
