# 0x06. Python - Classes and Objects

This project introduces Object-Oriented Programming (OOP) concepts in Python through the implementation of a `Square` class. Each task builds upon the previous one, gradually adding more functionality and demonstrating key OOP principles.

## Learning Objectives

At the end of this project, you should be able to explain:

- What is Object-Oriented Programming (OOP)
- What is a class and what is an object or instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python

## Requirements

- Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- All modules should have a documentation
- All classes should have a documentation
- All functions should have a documentation

## Project Structure

```
0x06-python-classes/
├── 0-square.py          # Empty Square class
├── 1-square.py          # Square class with private size attribute
├── 2-square.py          # Square class with size validation
├── 3-square.py          # Square class with area calculation
├── 4-square.py          # Square class with getter and setter
├── 5-square.py          # Square class with printing functionality
├── 6-square.py          # Square class with position attribute
├── 1-main.py           # Test file for task 1
├── 2-main.py           # Test file for task 2
├── 3-main.py           # Test file for task 3
├── 4-main.py           # Test file for task 4
├── 5-main.py           # Test file for task 5
├── 6-main.py           # Test file for task 6
└── README.md           # This file
```

## Tasks

### 0. My first square
**File:** `0-square.py`

Write an empty class `Square` that defines a square.

**Requirements:**
- You are not allowed to import any module

### 1. Square with size
**File:** `1-square.py`

Write a class `Square` that defines a square by a private instance attribute `size`.

**Requirements:**
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

### 2. Size validation
**File:** `2-square.py`

Write a class `Square` that defines a square by a private instance attribute `size` with proper validation.

**Requirements:**
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer"
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0"
- You are not allowed to import any module

### 3. Area of a square
**File:** `3-square.py`

Write a class `Square` that defines a square by a private instance attribute `size` and provides a method to calculate area.

**Requirements:**
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Size validation (same as task 2)
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

### 4. Access and update private attribute
**File:** `4-square.py`

Write a class `Square` that defines a square by a private instance attribute `size` with getter and setter properties.

**Requirements:**
- Private instance attribute: `size`
- Property `def size(self):` to retrieve it
- Property setter `def size(self, value):` to set it
- Size validation in the setter
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

### 5. Printing a square
**File:** `5-square.py`

Write a class `Square` that defines a square and can print itself using the `#` character.

**Requirements:**
- All previous requirements
- Public instance method: `def my_print(self):` that prints the square with the character `#`
- If `size` is equal to 0, print an empty line
- You are not allowed to import any module

### 6. Coordinates of a square
**File:** `6-square.py`

Write a class `Square` that defines a square with size and position attributes.

**Requirements:**
- Private instance attribute: `size` and `position`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Property getters and setters for both `size` and `position`
- Position must be a tuple of 2 positive integers
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints the square with the character `#` using position
- You are not allowed to import any module

## Usage Examples

### Basic Usage
```python
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print(my_square.size)
except Exception as e:
    print(e)
```

### Printing a Square
```python
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square = Square(10)
my_square.my_print()
```

### Square with Position
```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()
```

## Testing

Each task includes a corresponding main file for testing:

```bash
# Test task 1
./1-main.py

# Test task 2
./2-main.py

# Test task 3
./3-main.py

# And so on...
```

## Author

This project is part of the ALX Higher Level Programming curriculum, focusing on Python classes and object-oriented programming concepts.

## License

This project is part of the ALX curriculum and is intended for educational purposes.