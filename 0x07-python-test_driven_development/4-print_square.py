#!/usr/bin/python3
"""Defines a square-printing function.

This module provides functionality for printing squares made of '#' characters
to stdout. The squares are printed with customizable dimensions based on the
provided size parameter.
"""


def print_square(size):
    """Print a square pattern using '#' characters to stdout.
    
    Creates and prints a square of '#' characters with the specified dimensions.
    Each row contains 'size' number of '#' characters, and there are 'size'
    number of rows total. If size is 0, nothing is printed.
    
    Args:
        size (int): The height and width of the square to print. Must be a 
            non-negative integer. A size of 0 will print nothing.
    
    Returns:
        None: This function doesn't return a value, it prints to stdout.
    
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    
    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        
        >>> print_square(2)
        ##
        ##
        
        >>> print_square(1)
        #
        
        >>> print_square(0)
        (prints nothing)
    
    Note:
        The function prints each row immediately and adds a newline at the end
        of each row. No trailing spaces are added to the rows.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")