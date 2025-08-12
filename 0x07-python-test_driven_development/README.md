# 0x07. Python - Test-driven development

This project introduces the concept of Test-Driven Development (TDD) in Python. You'll learn to write tests before implementing functions, use doctest for embedded testing, and develop robust, well-documented code following TDD principles.

## Background Context

**Important notice on intranet checks for Python projects**

Starting from today:
- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
- The intranet checks for Python projects won't be released before their first deadline, in order for you to focus on TDD and think about all possible edge cases

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What's an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

## Files Description

### Implementation Files

| File | Description |
|------|-------------|
| `0-add_integer.py` | Function that adds 2 integers |
| `2-matrix_divided.py` | Function that divides all elements of a matrix |
| `3-say_my_name.py` | Function that prints "My name is <first name> <last name>" |
| `4-print_square.py` | Function that prints a square with the character # |
| `5-text_indentation.py` | Function that prints a text with 2 new lines after each of these characters: ., ? and : |
| `6-max_integer.py` | Function to find the max integer in a list |

### Test Files

| File | Description |
|------|-------------|
| `tests/0-add_integer.txt` | Doctest file for add_integer function |
| `tests/2-matrix_divided.txt` | Doctest file for matrix_divided function |
| `tests/3-say_my_name.txt` | Doctest file for say_my_name function |
| `tests/4-print_square.txt` | Doctest file for print_square function |
| `tests/5-text_indentation.txt` | Doctest file for text_indentation function |
| `tests/6-max_integer_test.py` | Unittest file for max_integer function |

### Main Test Files

| File | Description |
|------|-------------|
| `0-main.py` | Test file for add_integer function |
| `2-main.py` | Test file for matrix_divided function |
| `3-main.py` | Test file for say_my_name function |
| `4-main.py` | Test file for print_square function |
| `5-main.py` | Test file for text_indentation function |
| `6-main.py` | Test file for max_integer function |

## Tasks

### 0. Integers addition
**File**: `0-add_integer.py`, `tests/0-add_integer.txt`

Write a function that adds 2 integers.

**Prototype**: `def add_integer(a, b=98):`
**Requirements**:
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

### 1. Divide a matrix
**File**: `2-matrix_divided.py`, `tests/2-matrix_divided.txt`

Write a function that divides all elements of a matrix.

**Prototype**: `def matrix_divided(matrix, div):`
**Requirements**:
- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
- `div` can't be equal to 0, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module

### 2. Say my name
**File**: `3-say_my_name.py`, `tests/3-say_my_name.txt`

Write a function that prints `My name is <first name> <last name>`

**Prototype**: `def say_my_name(first_name, last_name=""):`
**Requirements**:
- `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
- You are not allowed to import any module

### 3. Print square
**File**: `4-print_square.py`, `tests/4-print_square.txt`

Write a function that prints a square with the character `#`.

**Prototype**: `def print_square(size):`
**Requirements**:
- `size` is the size length of the square
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
- if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
- You are not allowed to import any module

### 4. Text indentation
**File**: `5-text_indentation.py`, `tests/5-text_indentation.txt`

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

**Prototype**: `def text_indentation(text):`
**Requirements**:
- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module

### 5. Max integer - Unittest
**File**: `tests/6-max_integer_test.py`

Since the beginning you have been creating "Interactive tests". For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`

**Requirements**:
- Your test file should be inside a folder `tests`
- You have to use the unittest module
- Your test file should be python files (extension: `.py`)
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
- All tests you make must be passable by the function below

## Test-Driven Development Process

### 1. Red Phase
Write a failing test first:
```python
def test_add_integer():
    """Test adding two integers"""
    result = add_integer(1, 2)
    assert result == 3
```

### 2. Green Phase
Write minimal code to make the test pass:
```python
def add_integer(a, b=98):
    """Add two integers"""
    return a + b
```

### 3. Refactor Phase
Improve the code while keeping tests passing:
```python
def add_integer(a, b=98):
    """Add two integers.
    
    Args:
        a: first integer or float
        b: second integer or float (default 98)
        
    Returns:
        The sum of a and b as integer
        
    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
```

## Doctest Examples

### Basic Doctest Format
```python
def add_integer(a, b=98):
    """Add two integers.
    
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    """
    # Function implementation
```

### Testing Edge Cases
```python
"""
Test edge cases in separate .txt file:

>>> add_integer(1.5, 2.5)
4

>>> add_integer("hello", 2)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer(1, None)
Traceback (most recent call last):
    ...
TypeError: b must be an integer
"""
```

## Usage Examples

### Testing add_integer
```python
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
```

### Testing matrix_divided
```python
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
```

### Testing say_my_name
```python
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
```

## Running Tests

### Running Doctest
```bash
python3 -m doctest ./tests/*
python3 -m doctest -v ./tests/0-add_integer.txt
```

### Running Unittest
```bash
python3 -m unittest tests.6-max_integer_test
python3 -m unittest tests.6-max_integer_test.TestMaxInteger.test_max_at_end
```

### Interactive Testing
```bash
python3
>>> from 0-add_integer import add_integer
>>> add_integer(1, 2)
3
```

## Key Concepts

### Test Types
- **Unit Tests**: Test individual functions in isolation
- **Integration Tests**: Test how components work together
- **Doctests**: Tests embedded in documentation strings
- **Interactive Tests**: Manual testing in Python interpreter

### Edge Cases to Consider
- **Boundary values**: 0, -1, maximum/minimum values
- **Invalid types**: None, strings when expecting numbers
- **Empty inputs**: empty lists, empty strings
- **Special values**: infinity, NaN for floats

### Error Handling Patterns
```python
# Type checking
if not isinstance(value, expected_type):
    raise TypeError("message")

# Value validation
if value < 0:
    raise ValueError("message")

# Zero division
if divisor == 0:
    raise ZeroDivisionError("message")
```

## Best Practices

### Writing Good Tests
1. **Test one thing at a time**
2. **Use descriptive test names**
3. **Include both positive and negative test cases**
4. **Test edge cases and boundary conditions**
5. **Keep tests independent**

### Documentation Standards
1. **Module docstrings**: Describe the module's purpose
2. **Function docstrings**: Describe parameters, return values, and exceptions
3. **Doctest examples**: Show typical usage and edge cases
4. **Clear error messages**: Help users understand what went wrong

### Code Quality
1. **Follow PEP 8 style guide**
2. **Use meaningful variable names**
3. **Keep functions small and focused**
4. **Handle errors gracefully**
5. **Write self-documenting code**

## Common Doctest Patterns

### Testing Exceptions
```python
>>> matrix_divided([[1, 2], [3, 4]], 0)
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
```

### Testing Output
```python
>>> print_square(3)
###
###
###
```

### Testing Return Values
```python
>>> matrix_divided([[1, 2], [3, 4]], 2)
[[0.5, 1.0], [1.5, 2.0]]
```

## Author
This project is part of the ALX Higher Level Programming curriculum.

## Resources
- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Unittest module](https://docs.python.org/3.4/library/unittest.html)
- [Interactive and non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)