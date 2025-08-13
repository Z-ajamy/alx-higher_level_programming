#!/usr/bin/python3
"""Defines a text-indentation function.

This module provides functionality for formatting text by adding line breaks
after specific punctuation marks and managing whitespace around these breaks.
The formatting creates visual separation between sentences and clauses.
"""


def text_indentation(text):
    """Print text with formatted line breaks after specific punctuation marks.
    
    Processes the input text character by character and adds two newlines after
    each occurrence of '.', '?', or ':'. Leading whitespace at the beginning
    of the text and trailing whitespace after punctuation marks are stripped.
    Existing newlines in the text are preserved.
    
    Args:
        text (str): The text string to format and print. Can contain any 
            characters including newlines, spaces, and punctuation marks.
    
    Returns:
        None: This function doesn't return a value, it prints the formatted
            text directly to stdout.
    
    Raises:
        TypeError: If text is not a string.
    
    Examples:
        >>> text_indentation("Hello. How are you? I am fine: thanks.")
        Hello.
        
        How are you?
        
        I am fine:
        
        thanks.
        
        >>> text_indentation("First sentence.    Second sentence.")
        First sentence.
        
        Second sentence.
        
        >>> text_indentation("No punctuation here")
        No punctuation here
    
    Note:
        - Leading spaces at the start of the text are automatically removed
        - Spaces immediately following '.', '?', or ':' are automatically removed
        - Each punctuation mark triggers exactly two newlines (one explicit, one implicit)
        - Existing newlines in the original text are preserved and printed as-is
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
