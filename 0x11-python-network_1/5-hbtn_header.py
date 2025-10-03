#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to it, and displays the value
of the 'X-Request-Id' header found in the response.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the URL from the first command-line argument
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Access the headers dictionary from the response object and safely get
    # the value of 'X-Request-Id'. The .get() method is preferred as it
    # returns None instead of raising an error if the key is not found.
    request_id = response.headers.get('X-Request-Id')

    # Print the value if it exists
    if request_id:
        print(request_id)
