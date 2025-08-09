#!/usr/bin/python3
"""
Module for file writing utilities.

This module provides utilities for writing text content to files with
UTF-8 encoding, including automatic file handling and character count reporting.
"""


def write_file(filename="", text=""):
    """
    Write text content to a file with UTF-8 encoding.
    
    This function opens a file in write mode with UTF-8 encoding, writes
    the specified text content to it, and returns the number of characters
    written. If the file doesn't exist, it will be created. If it exists,
    it will be overwritten. The file is automatically closed after writing
    due to the use of a context manager (with statement).
    
    Args:
        filename (str, optional): The path to the file to be written to.
                                 Defaults to an empty string.
        text (str, optional): The text content to write to the file.
                             Defaults to an empty string.
    
    Returns:
        int: The number of characters written to the file.
    
    Raises:
        FileNotFoundError: If the directory path for the file does not exist.
        PermissionError: If there are insufficient permissions to write to 
                        the file or create it in the specified location.
        IOError: If there are other I/O related errors during file operations.
        UnicodeEncodeError: If the text contains characters that cannot be
                           encoded in UTF-8 (rare, as UTF-8 supports most characters).
    
    Example:
        >>> chars_written = write_file("output.txt", "Hello, World!")
        >>> print(chars_written)
        13
        
        >>> write_file("empty.txt", "")
        0
        
        >>> write_file("unicode.txt", "Hello 世界")
        8
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
