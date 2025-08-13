#!/usr/bin/python3
"""Defines a name-printing function.

This module provides functionality for printing formatted names to stdout.
It handles both first and last names with proper string validation.
"""


def say_my_name(first_name, last_name=""):
    """Print a formatted name to stdout.
    
    Prints "My name is <first_name> <last_name>" to standard output.
    Both names are validated to ensure they are strings before printing.
    
    Args:
        first_name (str): The first name to print. Must be a string.
        last_name (str, optional): The last name to print. Defaults to empty string.
            Must be a string.
    
    Returns:
        None: This function doesn't return a value, it prints to stdout.
    
    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    
    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        
        >>> say_my_name("Walter", "White")
        My name is Walter White
        
        >>> say_my_name("Bob")
        My name is Bob 
    
    Note:
        If last_name is empty, the output will have a trailing space after first_name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))