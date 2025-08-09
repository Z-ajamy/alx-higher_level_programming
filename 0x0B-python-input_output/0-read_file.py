#!/usr/bin/python3
"""
Module for file reading utilities.

This module provides utilities for reading and displaying the contents
of text files, with automatic file handling and content output to stdout.
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file.
    
    This function opens a text file in read mode, reads its entire contents,
    and prints it to stdout. The file is automatically closed after reading
    due to the use of a context manager (with statement).
    
    Args:
        filename (str, optional): The path to the file to be read. 
                                 Defaults to an empty string.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IOError: If there are other I/O related errors during file operations.
        UnicodeDecodeError: If the file contains characters that cannot be 
                           decoded using the default encoding.
    
    Example:
        >>> read_file("example.txt")
        Hello, World!
        This is the content of example.txt
        
        >>> read_file()  # Attempts to read file with empty filename
        FileNotFoundError: [Errno 2] No such file or directory: ''
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")