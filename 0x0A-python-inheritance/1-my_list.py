#!/usr/bin/python3
"""
Module for extended list functionality.

This module provides a MyList class that extends the built-in list class
with additional methods for enhanced list operations and display functionality.
"""


class MyList(list):
    """
    A class that extends the built-in list with additional functionality.
    
    This class inherits all standard list methods and adds custom methods
    for enhanced list operations, including sorted display capabilities.
    
    Inherits from:
        list: The built-in Python list class.
    """
    
    def print_sorted(self):
        """
        Print the list elements in sorted order without modifying the original list.
        
        This method creates a sorted copy of the list and prints it to stdout.
        The original list remains unchanged. Elements are sorted using Python's
        default sorting behavior.
        
        Note:
            All elements in the list should be of comparable types to avoid
            TypeError during sorting.
        
        Example:
            >>> my_list = MyList([3, 1, 4, 1, 5])
            >>> my_list.print_sorted()
            [1, 1, 3, 4, 5]
            >>> print(my_list)  # Original list unchanged
            [3, 1, 4, 1, 5]
        """
        print(sorted(self))
