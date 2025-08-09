#!/usr/bin/python3
"""
Script for managing a persistent JSON list with command line arguments.

This script maintains a persistent list stored in a JSON file. It handles
different scenarios: when no arguments are provided (resets the list to empty),
and when arguments are provided (adds them to existing items). The script
loads existing items from the file if it exists, processes command line
arguments, and saves the updated list back to the file.
"""

if __name__ == "__main__":
    import os
    from sys import argv
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    
    # Define the path to the JSON file for persistent storage
    path = "add_item.json"

    # If no arguments provided, reset the list to empty
    if len(argv) == 1:
        save_to_json_file([], path)

    # Load existing list from file if it exists, otherwise start with empty list
    if os.path.exists(path):
        list1 = load_from_json_file(path)
    else:
        list1 = []
    
    # Combine existing list with new command line arguments (excluding script name)
    res = list1 + argv[1:]
    
    # Save the updated list back to the JSON file
    save_to_json_file(res, path)
    