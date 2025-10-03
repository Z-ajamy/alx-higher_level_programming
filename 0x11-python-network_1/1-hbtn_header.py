#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
import urllib.request
if argv[1]:
    with urllib.request.urlopen(argv[1]) as response:
        try:
            headers = response.headers
            responseID = headers["X-Request-Id"]

            if responseID:
                print(responseID)
        except urllib.error.URLError as e:
            pass
