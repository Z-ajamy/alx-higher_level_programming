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
