#!/usr/bin/python3
"""
Module: base_geometry

This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception indicating that
        the method is not implemented.

        Raises:
            Exception: If the method is called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        
        if not isinstance(value, int):
            raise TabError("<name> must be an integer")
        elif value <= 0:
            raise TabError("<name> must be greater than 0")
