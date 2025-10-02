#!/usr/bin/python3
"""
A script that fetches a URL and handles potential errors gracefully.
"""
import urllib.request
import urllib.error

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        
        decoded_data = data.decode("utf-8")
        print(f"\t- utf8 content: {decoded_data}")

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")

except urllib.error.URLError as e:
    print(f"Error: Failed to reach the server.")
    print(f"Reason: {e.reason}")

except UnicodeDecodeError:
    print("Error: Could not decode the response body using UTF-8.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
