#!/usr/bin/python3
"""
Module: file_reader

This module defines a function to read the contents of a file.
"""


def read_file(filename=""):
    """Reads the contents of a file and prints it to the console.

    Args:
        filename (str): The name of the file to read from. Defaults to an empty string.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
