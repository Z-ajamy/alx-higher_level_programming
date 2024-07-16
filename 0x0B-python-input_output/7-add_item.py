#!/usr/bin/python3
"""
Module: add_item

This script adds command-line arguments to a list and saves it to a JSON file.
"""


from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Load the existing list from the JSON file
        to_json = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        to_json = []

    # Add all command-line arguments to the list
    to_json.extend(argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(to_json, 'add_item.json')
