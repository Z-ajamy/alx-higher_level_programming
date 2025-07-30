# 0x00. Python - Hello, World

## ALX Higher Level Programming

## About
This is the first project in the ALX Higher Level Programming track, focusing on Python basics and the fundamentals of programming with Python.

## Resources
**Read or watch:**
- The Python tutorial (only the first three chapters below)
- Whetting Your Appetite
- Using the Python Interpreter
- An Informal Introduction to Python (Read up until "3.1.2. Strings" included)
- How To Use String Formatters in Python 3
- Learn to Program
- Pycodestyle – Style Guide for Python Code

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name 'Python' come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called lists.h
- All your header files should be include guarded

## Tasks

### 0. Run Python file
**Mandatory**

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

```bash
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```

**File:** `0-run`

### 1. Run inline
**Mandatory**

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

```bash
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```

**File:** `1-run_inline`

### 2. Hello, print
**Mandatory**

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

- Use the function `print`

```bash
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

**File:** `2-print.py`

### 3. Print integer
**Mandatory**

Complete this source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

```python
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE
```

- You can find the source code here
- The output of the script should be:
  - the number, followed by `Battery street`
  - followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings

```bash
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

**File:** `3-print_number.py`

### 4. Print float
**Mandatory**

Complete this source code in order to print the float stored in the variable number with a precision of 2 digits.

```python
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE
```

- You can find the source code here
- The output of the script should be:
  - `Float:` followed by the number with only 2 digits
  - followed by a new line
- You are not allowed to cast the variable `number` into a string
- You have to use f-strings

```bash
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

**File:** `4-print_float.py`

### 5. Print string
**Mandatory**

Complete this source code in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

```python
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE
```

- You can find the source code here
- The output of the script should be:
  - 3 times the value of `str`
  - followed by a new line
  - followed by the first 9 characters of `str`
  - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

```bash
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
```

**File:** `5-print_string.py`

## Repository
- **GitHub repository:** `alx-higher_level_programming`
- **Directory:** `0x00-python-hello_world`

## Author
**Z-ajamy** - ALX Student
- GitHub: [@Z-ajamy](https://github.com/Z-ajamy)

## Acknowledgments
- ALX School for providing the curriculum and learning environment
- Peers and mentors for collaboration and support
- The broader programming community for resources and inspiration

## License
This project is part of the ALX curriculum and follows the school's academic policies regarding code sharing and collaboration.

---

*This repository represents ongoing learning and development in higher-level programming concepts through the ALX program.*