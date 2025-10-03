#!/usr/bin/python3

"""
HTTP request script to retrieve and display X-Request-Id header.
This module sends an HTTP request to a URL provided as a command-line argument
and attempts to extract and display the X-Request-Id header from the response.
The X-Request-Id header is commonly used for request tracking and debugging in
web services.

The script expects one command-line argument:
    - URL to send the HTTP request to

Dependencies:
    - urllib.request for HTTP operations
    - sys for command-line argument access

Typical usage example:
    $ python3 script.py https://api.example.com/endpoint

Note:
    The script silently handles URLError exceptions without output.
    If the X-Request-Id header is not present, no output is produced.
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
