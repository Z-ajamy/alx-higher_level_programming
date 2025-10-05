#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # The first argument is the username, the second is the personal access token
    username = sys.argv[1]
    password = sys.argv[2]

    # Create an authentication object for Basic Authentication
    auth = HTTPBasicAuth(username, password)

    # The GitHub API endpoint to get information about the authenticated user
    url = "https://api.github.com/user"

    # Send a GET request to the API with the authentication credentials
    response = requests.get(url, auth=auth)

    # Parse the JSON response into a Python dictionary
    user_data = response.json()

    # Safely get the 'id' from the dictionary and print it
    # The .get() method is used to avoid an error if 'id' is not present
    print(user_data.get("id"))
