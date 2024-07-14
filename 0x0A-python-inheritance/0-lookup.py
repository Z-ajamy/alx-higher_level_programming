#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods
        available on the object.
    """
    return dir(obj)
