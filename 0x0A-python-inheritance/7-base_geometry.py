#!/usr/bin/python3
"""
Module: base_geometry

This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception indicating that the method
        is not implemented.

        Raises:
            Exception: If the method is called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the input value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
