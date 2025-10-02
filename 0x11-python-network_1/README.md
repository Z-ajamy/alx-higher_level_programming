# 0x11. Python - Network #1

## Description
This project builds upon the networking concepts from the previous project. Instead of using `curl`, you'll be using Python packages (`urllib` and `requests`) to interact with APIs and fetch internet resources. You'll learn how to make HTTP requests, handle responses, work with JSON data, and interact with APIs using Python.

## Learning Objectives
At the end of this project, you should be able to explain:

### General
- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` (which is simpler than `urllib`)
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use `get` to access to dictionary value by key (it won't throw an exception if the key doesn't exist in the dictionary)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks

### 0. What's my status? #0
**File:** `0-hbtn_status.py`

Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using the `urllib` package.

**Requirements:**
- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before each line)
- You must use a `with` statement

**Example:**
```bash
$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

---

### 1. Response header value #0
**File:** `1-hbtn_header.py`

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

**Requirements:**
- You must use the packages `urllib` and `sys`
- You are not allowed to import packages other than `urllib` and `sys`
- The value of this variable is different for each request
- You don't need to check arguments passed to the script (number or type)
- You must use a `with` statement

**Example:**
```bash
$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
```

---

### 2. POST an email #0
**File:** `2-post_email.py`

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`).

**Requirements:**
- The email must be sent in the `email` variable
- You must use the packages `urllib` and `sys`
- You are not allowed to import packages other than `urllib` and `sys`
- You don't need to check arguments passed to the script (number or type)
- You must use the `with` statement

**Example:**
```bash
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

---

### 3. Error code #0
**File:** `3-error_code.py`

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

**Requirements:**
- You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- You must use the packages `urllib` and `sys`
- You are not allowed to import other packages than `urllib` and `sys`
- You don't need to check arguments passed to the script (number or type)
- You must use the `with` statement

**Example:**
```bash
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

---

### 4. What's my status? #1
**File:** `4-hbtn_status.py`

Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using the `requests` package.

**Requirements:**
- You must use the package `requests`
- You are not allowed to import packages other than `requests`
- The body of the response must be displayed like the following example (tabulation before each line)

**Example:**
```bash
$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
```

---

### 5. Response header value #1
**File:** `5-hbtn_header.py`

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.

**Requirements:**
- You must use the packages `requests` and `sys`
- You are not allowed to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- You don't need to check script arguments (number and type)

**Example:**
```bash
$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b69-4d7a4f3e5d42
$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
```

---

### 6. POST an email #1
**File:** `6-post_email.py`

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

**Requirements:**
- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don't need to error check arguments passed to the script (number or type)

**Example:**
```bash
$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

---

### 7. Error code #1
**File:** `7-error_code.py`

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

**Requirements:**
- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don't need to check arguments passed to the script (number or type)

**Example:**
```bash
$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

---

### 8. Search API
**File:** `8-json_api.py`

Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

**Requirements:**
- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
  - Display `Not a valid JSON` if the JSON is invalid
  - Display `No result` if the JSON is empty
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`

**Example:**
```bash
$ ./8-json_api.py 
No result
$ ./8-json_api.py a
[8446] amnirqhtfjq
$ ./8-json_api.py 2
No result
$ ./8-json_api.py b
[7094] bmofakakhke
```

---

### 9. My GitHub!
**File:** `10-my_github.py`

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your `id`.

**Requirements:**
- You must use Basic Authentication with a personal access token as password to access to your information (only `read:user` permission is needed)
- The first argument will be your username
- The second argument will be your password (in your case, a personal access token as password)
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don't need to check arguments passed to the script (number or type)

**Example:**
```bash
$ ./10-my_github.py papamuziko cisfun
2531536
$ ./10-my_github.py papamuziko wrong_pwd
None
```

**Note:** You need to create a Personal Access Token on GitHub:
1. Go to Settings → Developer settings → Personal access tokens
2. Generate new token with `read:user` scope
3. Use this token as your password

---

## urllib vs requests

### urllib (Standard Library)
```python
import urllib.request
import urllib.parse

# GET request
with urllib.request.urlopen('http://example.com') as response:
    html = response.read()

# POST request
data = urllib.parse.urlencode({'key': 'value'}).encode()
req = urllib.request.Request('http://example.com', data=data)
with urllib.request.urlopen(req) as response:
    result = response.read()
```

**Pros:**
- Part of Python standard library (no installation needed)
- Good for simple tasks

**Cons:**
- More verbose
- Requires more boilerplate code
- Less intuitive API

### requests (Third-party Library)
```python
import requests

# GET request
response = requests.get('http://example.com')
print(response.text)

# POST request
response = requests.post('http://example.com', data={'key': 'value'})
print(response.text)

# JSON handling
response = requests.get('http://api.example.com/data')
data = response.json()
```

**Pros:**
- Much simpler and more intuitive
- Built-in JSON support
- Automatic encoding
- Better error handling
- Session support

**Cons:**
- Requires installation (`pip install requests`)

## Installation

### Installing requests
```bash
$ pip3 install requests
```

Or on Ubuntu:
```bash
$ sudo apt-get install python3-requests
```

## Code Examples

### GET Request with urllib
```python
#!/usr/bin/python3
"""Fetches a URL using urllib"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
```

### GET Request with requests
```python
#!/usr/bin/python3
"""Fetches a URL using requests"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
```

### Error Handling
```python
#!/usr/bin/python3
"""Handles HTTP errors"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
```

## Testing

You can set up a simple Flask server for testing:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return 'OK'

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    return f'Your email is: {email}'

@app.route('/status_401')
def status_401():
    return 'Unauthorized', 401

@app.route('/search_user', methods=['POST'])
def search_user():
    q = request.form.get('q', '')
    if q:
        return jsonify({"id": 8446, "name": "amnirqhtfjq"})
    return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Tips

1. **Always use `with` statement with urllib** - Ensures proper resource cleanup
2. **requests is simpler** - Use it when you can
3. **Handle errors gracefully** - Check status codes and handle exceptions
4. **Use `.json()` method** - When working with JSON APIs using requests
5. **Read the documentation** - Both urllib and requests have excellent docs
6. **Test with a local server** - Use Flask or similar to test your scripts
7. **Use `.get()` for dictionaries** - Safer than direct key access

## Common HTTP Status Codes

- **200** - OK (Success)
- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **500** - Internal Server Error
- **503** - Service Unavailable

## Resources

- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Requests package documentation](https://requests.readthedocs.io/)
- [urllib documentation](https://docs.python.org/3/library/urllib.html)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [GitHub API documentation](https://docs.github.com/en/rest)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
