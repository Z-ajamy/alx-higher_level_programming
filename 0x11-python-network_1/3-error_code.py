#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""

import urllib.request, urllib.error, sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as request:
            print(request.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except (IndexError, urllib.error.URLError) as e:
        pass
