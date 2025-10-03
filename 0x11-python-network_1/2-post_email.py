#!/usr/bin/python3
"""
A script that sends a POST request with an email and displays the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = sys.argv[2]

        data_dic = {"email": email}
        
        data_str = urllib.parse.urlencode(data_dic)
        data_byte = data_str.encode('ascii')

        req = urllib.request.Request(url, data=data_byte)
        with urllib.request.urlopen(req) as response:
            response_data_byte = response.read()
            
            response_data_str = response_data_byte.decode("utf-8")
            
            print(response_data_str)
            
    except (IndexError, urllib.error.URLError) as e:
        pass
