#!/usr/bin/python3
"""
Module: base

This module defines the Base class for object management.

The Base class includes a mechanism to manage object IDs automatically
if not provided during initialization.

Classes:
    Base: A class that manages object creation and IDs.

Usage:
    from base import Base

    # Example usage
    obj1 = Base()       # Automatically assigns an ID
    obj2 = Base(100)    # Assigns a specific ID
"""


class Base:
    """Base class for object management.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number
            of instances created or assigned with an ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object with an optional ID.

        Args:
            id (int or None): ID to assign to the object. If None,
            assigns a new
                incremented value of __nb_objects.
        """
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            type(self).__nb_objects = self.id
