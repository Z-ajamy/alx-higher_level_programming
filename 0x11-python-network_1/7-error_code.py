#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to it, and displays
the body of the response. If the HTTP status code is 400 or greater,
it prints an error message with the status code instead.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the URL from the first command-line argument
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the status code indicates an error (>= 400)
    if response.status_code >= 400:
        # If there is an error, print the required error message
        print(f"Error code: {response.status_code}")
    else:
        # If the request was successful, print the body of the response
        print(response.text)
