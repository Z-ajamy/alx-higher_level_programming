#!/usr/bin/python3
"""
Module: file_writer

This module defines a function to write text to a file.
"""

def write_file(filename="", text=""):
    """Writes the given text to a file.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
