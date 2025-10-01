# 0x10. Python - Network #0

## Description
This project introduces the fundamentals of networking and HTTP requests using command-line tools and Python. You'll learn how to make HTTP requests, understand HTTP methods, headers, and body, and work with URLs. The project uses `curl` for making requests and Python for algorithmic problem-solving.

## Learning Objectives
At the end of this project, you should be able to explain:

### General
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (`wc -l file` should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly `#!/bin/bash`
- The second line of all your Bash scripts should be a comment explaining what the script does
- All `curl` commands must have the option `-s` (silent mode)
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Python files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version 2.8.*)
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method

## Tasks

### 0. cURL body size
**File:** `0-body_size.sh`

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

**Requirements:**
- The size must be displayed in bytes
- You have to use `curl`

**Example:**
```bash
$ ./0-body_size.sh 0.0.0.0:5000
10
```

---

### 1. cURL to the end
**File:** `1-body.sh`

Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response.

**Requirements:**
- Display only body of a 200 status code response
- You have to use `curl`

**Example:**
```bash
$ ./1-body.sh 0.0.0.0:5000/route_1
Route 2
```

---

### 2. cURL Method
**File:** `2-delete.sh`

Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response.

**Requirements:**
- You have to use `curl`

**Example:**
```bash
$ ./2-delete.sh 0.0.0.0:5000/route_3
I'm a DELETE request
```

---

### 3. cURL only methods
**File:** `3-methods.sh`

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

**Requirements:**
- You have to use `curl`

**Example:**
```bash
$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
```

---

### 4. cURL headers
**File:** `4-header.sh`

Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response.

**Requirements:**
- A header variable `X-School-User-Id` must be sent with the value `98`
- You have to use `curl`

**Example:**
```bash
$ ./4-header.sh 0.0.0.0:5000/route_5
Hello School!
```

---

### 5. cURL POST parameters
**File:** `5-post_params.sh`

Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response.

**Requirements:**
- A variable `email` must be sent with the value `test@gmail.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`
- You have to use `curl`

**Example:**
```bash
$ ./5-post_params.sh 0.0.0.0:5000/route_6
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
```

---

### 6. Find a peak
**Files:** `6-peak.py`, `6-peak.txt`

Write a function that finds a peak in a list of unsorted integers.

**Requirements:**
- Prototype: `def find_peak(list_of_integers):`
- You are not allowed to import any module
- Your algorithm must have the lowest complexity (hint: you don't need to go through all numbers to find a peak)
- `6-peak.py` must contain the function
- `6-peak.txt` must contain the complexity of your algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`

**Note:** There may be more than one peak in the list, you need to find only one.

**Example:**
```python
#!/usr/bin/python3
""" Test file """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
```

**Output:**
```
6
3
2
None
2
4
```

## HTTP Basics

### URL Structure
```
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument
```

- **Protocol/Scheme:** `http://` or `https://`
- **Domain:** `www.example.com`
- **Port:** `:80` (optional, default is 80 for HTTP, 443 for HTTPS)
- **Path:** `/path/to/myfile.html`
- **Query String:** `?key1=value1&key2=value2`
- **Fragment:** `#SomewhereInTheDocument`

### HTTP Methods
- **GET:** Retrieve data from a server
- **POST:** Send data to a server
- **PUT:** Update data on a server
- **DELETE:** Delete data from a server
- **HEAD:** Get headers only (no body)
- **OPTIONS:** Get supported HTTP methods
- **PATCH:** Partially update data

### HTTP Status Codes
- **1xx:** Informational
- **2xx:** Success (200 OK, 201 Created, 204 No Content)
- **3xx:** Redirection (301 Moved Permanently, 302 Found)
- **4xx:** Client Error (400 Bad Request, 401 Unauthorized, 404 Not Found)
- **5xx:** Server Error (500 Internal Server Error, 503 Service Unavailable)

## cURL Command Examples

### Basic GET request
```bash
curl http://example.com
```

### Silent mode (no progress bar)
```bash
curl -s http://example.com
```

### Save response to file
```bash
curl -o output.html http://example.com
```

### Follow redirects
```bash
curl -L http://example.com
```

### Send custom headers
```bash
curl -H "X-Custom-Header: value" http://example.com
```

### POST request with data
```bash
curl -X POST -d "param1=value1&param2=value2" http://example.com
```

### DELETE request
```bash
curl -X DELETE http://example.com/resource
```

### Get only headers
```bash
curl -I http://example.com
```

### Show response headers with body
```bash
curl -i http://example.com
```

### Get allowed HTTP methods
```bash
curl -X OPTIONS -i http://example.com
```

## Testing Your Scripts

Most of these scripts will be tested against a local server. You can set up a simple Flask server for testing:

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/route_1')
def route_1():
    return "Route 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Tips

1. **Use `-s` flag with curl** - Required for silent mode (no progress meter)
2. **Test your scripts** - Make sure they work with different URLs
3. **Check line count** - Bash scripts must be exactly 3 lines (including shebang and comment)
4. **Read curl documentation** - `man curl` or `curl --help`
5. **Handle edge cases** - Consider what happens with invalid URLs or server errors

## Resources

- [HTTP (HyperText Transfer Protocol)](https://www.w3.org/Protocols/)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Using cURL to debug](https://curl.se/docs/manual.html)
- [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- [Python requests module](https://requests.readthedocs.io/)

## Author
This project is part of the ALX Software Engineering Program.

## License
This project is licensed under the terms of the ALX Software Engineering Program.
