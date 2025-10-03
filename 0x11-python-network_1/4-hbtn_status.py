#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status using the requests
package and displays the response body in a specific format.
"""
import requests


if __name__ == "__main__":
    # Define the target URL
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Get the body of the response as a string (requests decodes it for us)
    content_text = response.text
    
    # Print the output in the required format using f-strings for clarity
    print("Body response:")
    print(f"\t- type: {type(content_text)}")
    print(f"\t- content: {content_text}")
