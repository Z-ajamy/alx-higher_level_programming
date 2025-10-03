#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request
if sys.argv[1]:
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
        
            headers = response.headers
            responseID = headers.get("X-Request-Id")

            if responseID:
                print(responseID)
    except Exception as e:
        pass
