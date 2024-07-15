#!/usr/bin/python3
"""
Module: file_writer

This module defines a function to write text to a file.
"""


def write_file(filename="", text=""):
    """Writes text to a file, appending if the file already exists.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
