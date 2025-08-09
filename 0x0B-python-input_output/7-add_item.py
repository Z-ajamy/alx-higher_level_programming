#!/usr/bin/python3
"""
Script for adding command line arguments to a persistent JSON list.

This script maintains a persistent list stored in a JSON file. It loads
existing items from the file (if it exists), adds new command line arguments
to the list, saves the updated list back to the file, and prints the result.
The JSON file serves as a persistent storage for accumulating items across
multiple script executions.
"""

if __name__ == "__main__":
    import os
    from sys import argv
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file 
    
    # Define the path to the JSON file for persistent storage
    path = "add_item.json"
    
    # Load existing list from file if it exists, otherwise start with empty list
    if os.path.exists(path):
        list1 = load_from_json_file(path)
    else:
        list1 = []
    
    # Combine existing list with new command line arguments (excluding script name)
    res = list1 + argv[1:]
    
    # Save the updated list back to the JSON file
    save_to_json_file(res, path)
    
    # Display the updated list
    print(res)
    