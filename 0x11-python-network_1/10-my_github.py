#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and a personal access token)
and uses the GitHub API to display the user's ID.
"""
import sys
import requests


if __name__ == "__main__":
    # Get username and Personal Access Token (PAT) from command-line arguments
    username = sys.argv[1]
    pat = sys.argv[2]

    # The API endpoint to get the authenticated user's information
    url = 'https://api.github.com/user'

    # Send the GET request with Basic Authentication using the username and PAT
    response = requests.get(url, auth=(username, pat))

    # The .json() method will parse the response. If the request was successful,
    # the JSON will contain user data. If authentication failed, the JSON
    # will contain an error message but not an 'id' key.
    # In either case, .get('id') will safely return the ID or None.
    try:
        json_response = response.json()
        print(json_response.get('id'))
    except requests.exceptions.JSONDecodeError:
        # If the response is not JSON at all (e.g., server error page)
        print(None)
