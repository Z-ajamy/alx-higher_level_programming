# ALX Higher Level Programming: Python Import & Modules

## Overview

This module covers Python's import system and module structure. Understanding how to organize code into modules and import functionality is crucial for writing maintainable and reusable Python programs.

## Learning Objectives

By the end of this module, you should be able to:

- Understand what modules and packages are in Python
- Import modules using different methods
- Create your own modules and packages
- Use the `__name__ == "__main__"` idiom
- Understand Python's module search path
- Handle import errors gracefully
- Use command-line arguments in Python scripts

## 1. Introduction to Modules

### What is a Module?

A module in Python is simply a file containing Python code. It can define functions, classes, and variables, and can also include runnable code. Modules help organize related code and promote code reusability.

### Why Use Modules?

- **Code Reusability**: Write once, use many times
- **Organization**: Keep related functionality together
- **Namespace Management**: Avoid naming conflicts
- **Maintainability**: Easier to debug and update code
- **Collaboration**: Multiple developers can work on different modules

## 2. Basic Import Statements

### Simple Import

```python
# Importing the entire module
import math

# Using functions from the module
result = math.sqrt(16)
print(result)  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793
```

### From Import

```python
# Importing specific functions/variables
from math import sqrt, pi

# Using imported functions directly
result = sqrt(16)
print(result)  # Output: 4.0
print(pi)      # Output: 3.141592653589793
```

### Import with Alias

```python
# Importing with an alias
import math as m

result = m.sqrt(16)
print(result)  # Output: 4.0

# Importing specific items with alias
from math import sqrt as square_root

result = square_root(16)
print(result)  # Output: 4.0
```

### Import All (Use with Caution)

```python
# Importing everything from a module
from math import *

result = sqrt(16)
print(pi)
# Note: This can lead to namespace pollution and is generally discouraged
```

## 3. Common Built-in Modules

### Math Module

```python
import math

# Mathematical functions
print(math.sqrt(25))      # Square root: 5.0
print(math.pow(2, 3))     # Power: 8.0
print(math.factorial(5))  # Factorial: 120
print(math.ceil(4.3))     # Ceiling: 5
print(math.floor(4.7))    # Floor: 4

# Mathematical constants
print(math.pi)            # Pi: 3.141592653589793
print(math.e)             # Euler's number: 2.718281828459045
```

### Random Module

```python
import random

# Generate random numbers
print(random.random())           # Random float between 0 and 1
print(random.randint(1, 10))     # Random integer between 1 and 10
print(random.uniform(1.0, 10.0)) # Random float between 1.0 and 10.0

# Work with sequences
colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))     # Random choice from list
random.shuffle(colors)           # Shuffle list in place
print(colors)

# Random sample
numbers = list(range(1, 11))
print(random.sample(numbers, 3)) # Random sample of 3 elements
```

### OS Module

```python
import os

# Current working directory
print(os.getcwd())

# Environment variables
print(os.environ.get('HOME'))  # Get HOME environment variable
print(os.environ.get('USER'))  # Get USER environment variable

# Path operations
path = '/home/user/documents/file.txt'
print(os.path.dirname(path))   # Directory name
print(os.path.basename(path))  # Base name
print(os.path.splitext(path))  # Split extension

# Check if path exists
print(os.path.exists('/home'))
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/home'))
```

### Sys Module

```python
import sys

# Python version info
print(sys.version)
print(sys.version_info)

# Command line arguments
print(sys.argv)  # List of command line arguments

# Module search path
print(sys.path)

# Exit the program
# sys.exit(0)  # Uncomment to exit
```

### Datetime Module

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)

# Create specific date
birthday = datetime.date(1990, 5, 15)
print(birthday)

# Format dates
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(birthday.strftime("%B %d, %Y"))

# Date arithmetic
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)
```

## 4. Creating Your Own Modules

### Simple Module Example

Create a file called `calculator.py`:

```python
# calculator.py
"""
A simple calculator module
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Module-level variable
PI = 3.14159

# Module-level function that uses other functions
def circle_area(radius):
    """Calculate the area of a circle"""
    return PI * multiply(radius, radius)

if __name__ == "__main__":
    # This code runs only when the module is executed directly
    print("Testing calculator module...")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"5 / 3 = {divide(5, 3)}")
    print(f"Circle area (radius=5) = {circle_area(5)}")
```

### Using Your Module

Create another file to use your module:

```python
# main.py
import calculator

# Use functions from the calculator module
result1 = calculator.add(10, 5)
result2 = calculator.multiply(3, 4)

print(f"10 + 5 = {result1}")
print(f"3 * 4 = {result2}")
print(f"PI = {calculator.PI}")

# Alternative import methods
from calculator import subtract, PI
print(f"10 - 3 = {subtract(10, 3)}")

from calculator import circle_area as area
print(f"Circle area = {area(3)}")
```

## 5. The `__name__ == "__main__"` Idiom

### Understanding `__name__`

Every Python module has a built-in variable called `__name__`. When a module is imported, `__name__` is set to the module's name. When a module is run directly, `__name__` is set to `"__main__"`.

```python
# demo_module.py
print(f"This module's name is: {__name__}")

def say_hello():
    print("Hello from demo_module!")

if __name__ == "__main__":
    print("This module is being run directly!")
    say_hello()
else:
    print("This module is being imported!")
```

### Practical Example

```python
# utilities.py
"""Utility functions for string processing"""

def reverse_string(s):
    """Return the reverse of a string"""
    return s[::-1]

def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def capitalize_words(s):
    """Capitalize the first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())

def main():
    """Main function for testing"""
    test_string = "hello world"
    
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Vowel count: {count_vowels(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")

if __name__ == "__main__":
    main()
```

## 6. Command Line Arguments

### Using sys.argv

```python
# greeting.py
import sys

def main():
    # sys.argv[0] is the script name
    # sys.argv[1:] are the command line arguments
    
    if len(sys.argv) < 2:
        print("Usage: python greeting.py <name>")
        sys.exit(1)
    
    name = sys.argv[1]
    print(f"Hello, {name}!")
    
    # Handle multiple arguments
    if len(sys.argv) > 2:
        age = sys.argv[2]
        print(f"You are {age} years old.")

if __name__ == "__main__":
    main()

# Usage:
# python greeting.py Alice
# python greeting.py Bob 25
```

### Advanced Command Line Processing

```python
# calculator_cli.py
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_cli.py <num1> <operator> <num2>")
        print("Operators: +, -, *, /")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                sys.exit(1)
            result = num1 / num2
        else:
            print(f"Error: Unknown operator '{operator}'")
            sys.exit(1)
        
        print(f"{num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("Error: Please provide valid numbers")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Usage:
# python calculator_cli.py 5 + 3
# python calculator_cli.py 10 / 2
```

## 7. Module Search Path and PYTHONPATH

### Understanding Module Search

Python searches for modules in the following order:

1. Current directory
2. PYTHONPATH directories
3. Standard library directories
4. Site-packages directories

```python
# show_path.py
import sys

print("Python module search path:")
for i, path in enumerate(sys.path):
    print(f"{i + 1}. {path}")
```

### Modifying the Search Path

```python
import sys
import os

# Add a custom directory to the path
custom_path = "/path/to/my/modules"
if custom_path not in sys.path:
    sys.path.append(custom_path)

# Now you can import modules from the custom directory
# import my_custom_module
```

## 8. Error Handling with Imports

### Handling Import Errors

```python
# safe_import.py
try:
    import numpy as np
    print("NumPy is available")
    HAS_NUMPY = True
except ImportError:
    print("NumPy is not installed")
    HAS_NUMPY = False

try:
    from math import sqrt
    print("Math module is available")
except ImportError as e:
    print(f"Error importing math: {e}")

# Conditional functionality based on available modules
def calculate_mean(numbers):
    if HAS_NUMPY:
        return np.mean(numbers)
    else:
        return sum(numbers) / len(numbers)
```

### Optional Imports

```python
# optional_features.py
def get_random_number():
    try:
        import secrets  # More secure random number generation
        return secrets.randbelow(100)
    except ImportError:
        import random   # Fallback to standard random
        return random.randint(0, 99)

def format_json(data):
    try:
        import json
        return json.dumps(data, indent=2)
    except ImportError:
        return str(data)  # Fallback to string representation
```

## 9. Packages and Package Structure

### Creating a Package

A package is a directory containing multiple modules. It must contain an `__init__.py` file.

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### Package Example

Create the following structure:

```python
# mymath/__init__.py
"""
MyMath package for mathematical operations
"""

# Import key functions to package level
from .basic import add, subtract
from .advanced import power, factorial

__version__ = "1.0.0"
__author__ = "Your Name"

# mymath/basic.py
"""Basic mathematical operations"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# mymath/advanced.py
"""Advanced mathematical operations"""

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def fibonacci(n):
    """Generate first n fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
```

### Using the Package

```python
# Using the package
import mymath

# Use functions imported to package level
print(mymath.add(5, 3))
print(mymath.factorial(5))

# Import specific modules
from mymath import basic
print(basic.multiply(4, 5))

# Import specific functions
from mymath.advanced import fibonacci
print(fibonacci(10))

# Package information
print(f"Version: {mymath.__version__}")
print(f"Author: {mymath.__author__}")
```

## 10. Best Practices

### Import Organization

```python
# Good import organization
# 1. Standard library imports
import os
import sys
from datetime import datetime

# 2. Third-party imports
import requests
import numpy as np

# 3. Local application imports
from mymodule import myfunction
from . import sibling_module
```

### Avoiding Circular Imports

```python
# Instead of this (circular import):
# module_a.py
from module_b import function_b

# module_b.py  
from module_a import function_a

# Do this:
# common.py
def shared_function():
    pass

# module_a.py
from common import shared_function

# module_b.py
from common import shared_function
```

### Documentation and Type Hints

```python
# well_documented_module.py
"""
A well-documented module with type hints
"""

from typing import List, Optional, Union

def process_numbers(numbers: List[Union[int, float]]) -> float:
    """
    Process a list of numbers and return their average.
    
    Args:
        numbers: A list of integers or floats
        
    Returns:
        The average of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    return sum(numbers) / len(numbers)

def find_item(items: List[str], target: str) -> Optional[int]:
    """
    Find the index of an item in a list.
    
    Args:
        items: List of strings to search
        target: String to find
        
    Returns:
        Index of the item if found, None otherwise
    """
    try:
        return items.index(target)
    except ValueError:
        return None
```

## 11. Common ALX Exercises and Solutions

### Exercise 1: Simple Import

```python
# 0-add.py
#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

# add_0.py (separate file)
#!/usr/bin/python3
def add(a, b):
    return a + b
```

### Exercise 2: Command Line Arguments

```python
# 2-args.py
#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    argc = len(sys.argv) - 1  # Exclude script name
    
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
```

### Exercise 3: Calculator with Command Line

```python
# 100-my_calculator.py
#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    print("{} {} {} = {}".format(a, operator, b, result))

# calculator_1.py (separate file)
#!/usr/bin/python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b  # Integer division as per ALX requirements
```

### Exercise 4: Print Names from Module

```python
# 4-hidden_discovery.py
#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
```

### Exercise 5: Import Variable

```python
# 5-variable_load.py
#!/usr/bin/python3

if __name__ == "__main__":
    from variable_load_5 import a
    print(a)

# variable_load_5.py (separate file)
#!/usr/bin/python3
a = 98
```

## 12. Advanced Import Concepts

### Dynamic Imports

```python
# dynamic_import.py
import importlib

def load_module_dynamically(module_name):
    """Load a module dynamically at runtime"""
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError as e:
        print(f"Could not import {module_name}: {e}")
        return None

# Usage
math_module = load_module_dynamically('math')
if math_module:
    print(math_module.pi)
```

### Reloading Modules

```python
# reload_example.py
import importlib
import my_module

# After modifying my_module.py, reload it
importlib.reload(my_module)
```

### Module Attributes

```python
# module_info.py
import math

# Get information about a module
print(f"Module name: {math.__name__}")
print(f"Module file: {math.__file__}")
print(f"Module doc: {math.__doc__}")

# List all attributes
print("\nModule attributes:")
for attr in dir(math):
    if not attr.startswith('_'):
        print(f"  {attr}: {type(getattr(math, attr))}")
```

## Summary

This module covers Python's import system comprehensively. Key concepts include:

- **Basic Imports**: Different ways to import modules and their contents
- **Built-in Modules**: Common modules like math, random, os, sys, datetime
- **Custom Modules**: Creating and organizing your own modules
- **Command Line Arguments**: Using sys.argv to handle command line input
- **Packages**: Organizing related modules into packages
- **Best Practices**: Proper import organization and error handling
- **Advanced Topics**: Dynamic imports, module reloading, and introspection

Understanding these concepts is essential for writing modular, maintainable Python code and is fundamental to professional Python development.
