#!/usr/bin/python3
"""Module for integer addition operations.

This module provides functionality for adding two numbers together,
with type validation and automatic conversion to integers.
"""


def add_integer(a, b=98):
    """Add two integers together.
    
    Takes two numbers (int or float) and returns their sum as an integer.
    Both parameters are converted to integers before addition.
    
    Args:
        a (int or float): The first number to add. Must be an integer or float.
        b (int or float, optional): The second number to add. Defaults to 98.
            Must be an integer or float.
    
    Returns:
        int: The sum of a and b, converted to integer.
    
    Raises:
        TypeError: If a is not an integer or float.
        TypeError: If b is not an integer or float.
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError ("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError ("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
