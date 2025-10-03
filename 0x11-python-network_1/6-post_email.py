#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request with the
email as a parameter, and displays the body of the response using requests.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email_address = sys.argv[2]

    # Prepare the data payload as a dictionary. The key must be 'email'.
    payload = {'email': email_address}

    # Send the POST request. The `requests` library handles the data
    # encoding automatically when you pass a dictionary to the `data` parameter.
    response = requests.post(url, data=payload)

    # Print the body of the response. The `.text` attribute automatically
    # decodes the content based on the server's headers.
    print(response.text)
