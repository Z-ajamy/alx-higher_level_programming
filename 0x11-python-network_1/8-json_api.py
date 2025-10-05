#!/usr/bin/python3
"""
A script that takes in a letter, sends a POST request with the letter
as a parameter 'q', and processes the JSON response.
"""
import sys
import requests


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    payload = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data=payload)

    try:
        json_response = response.json()

        if json_response:
            user_id = json_response.get('id')
            user_name = json_response.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
