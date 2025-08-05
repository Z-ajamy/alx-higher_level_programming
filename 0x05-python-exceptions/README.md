# 0x05. Python - Exceptions

This project covers exception handling in Python, focusing on understanding and implementing proper error handling techniques.

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- What's the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What's the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Files Description

### Task Files

| File | Description |
|------|-------------|
| `0-safe_print_list.py` | Function that prints x elements of a list safely |
| `1-safe_print_integer.py` | Function that prints an integer with "{:d}".format() safely |
| `2-safe_print_list_integers.py` | Function that prints the first x elements of a list and only integers |
| `3-safe_print_division.py` | Function that divides 2 integers and prints the result safely |
| `4-list_division.py` | Function that divides element by element 2 lists safely |
| `5-raise_exception.py` | Function that raises a type exception |
| `6-raise_exception_msg.py` | Function that raises a name exception with a message |

### Test Files

| File | Description |
|------|-------------|
| `0-main.py` | Test file for task 0 |
| `1-main.py` | Test file for task 1 |
| `2-main.py` | Test file for task 2 |
| `3-main.py` | Test file for task 3 |
| `4-main.py` | Test file for task 4 |
| `5-main.py` | Test file for task 5 |
| `6-main.py` | Test file for task 6 |

## Key Concepts

### Exception Handling
Exception handling in Python is done using try-except blocks:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Cannot divide by zero!")
except Exception as e:
    # Handle any other exception
    print(f"An error occurred: {e}")
finally:
    # Code that always runs
    print("Cleanup code here")
```

### Common Exception Types
- `ValueError`: Raised when a function receives an argument of correct type but inappropriate value
- `TypeError`: Raised when an operation or function is applied to an object of inappropriate type
- `IndexError`: Raised when a sequence subscript is out of range
- `KeyError`: Raised when a dictionary key is not found
- `ZeroDivisionError`: Raised when division or modulo by zero takes place

### Raising Exceptions
You can raise exceptions manually using the `raise` statement:

```python
raise ValueError("This is a custom error message")
```

## Usage

To test any of the functions, run the corresponding main file:

```bash
./0-main.py
./1-main.py
# ... and so on
```

## Author

This project is part of the ALX Higher Level Programming curriculum.

## Repository

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x05-python-exceptions`