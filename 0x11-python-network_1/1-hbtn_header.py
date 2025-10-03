#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
import urllib.request
if argv[1]:
    """Process the URL provided as the first command-line argument.
    
    Opens an HTTP connection to the specified URL and attempts to extract
    the X-Request-Id header from the response. The connection is automatically
    closed using the context manager.
    
    Args:
        argv[1] (str): The URL to send the HTTP request to.
        
    Prints:
        The value of the X-Request-Id header if present in the response.
        
    Raises:
        urllib.error.URLError: Silently caught and ignored if the request fails.
    """
    with urllib.request.urlopen(argv[1]) as response:
        try:
            """Extract headers from the HTTP response."""
            headers = response.headers
            responseID = headers["X-Request-Id"]

            if responseID:
                """Print the X-Request-Id value if it exists and is truthy."""
                print(responseID)
        except urllib.error.URLError as e:
            """Silently handle any URL-related errors during the request."""
            pass
