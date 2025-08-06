# 0x08. Python - More Classes and Objects

This project explores advanced Object-Oriented Programming concepts in Python, building upon the foundation from the previous classes project. We'll implement a `Rectangle` class with progressive enhancements, introducing class attributes, static methods, class methods, and special methods.

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
- What are the special `__str__` and `__repr__` methods and how to use them
- What is the difference between `__str__` and `__repr__`
- What is a class attribute
- What is the difference between an object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Requirements

### General
- Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

## Project Structure

```
0x08-python-more_classes/
├── 0-rectangle.py       # Empty Rectangle class
├── 1-rectangle.py       # Rectangle class with width and height
├── 2-rectangle.py       # Rectangle with area and perimeter methods
├── 3-rectangle.py       # Rectangle with string representation
├── 4-rectangle.py       # Rectangle with repr method
├── 5-rectangle.py       # Rectangle with deletion message
├── 6-rectangle.py       # Rectangle with instance counter
├── 7-rectangle.py       # Rectangle with print symbol customization
├── 8-rectangle.py       # Rectangle with comparison methods
├── 9-rectangle.py       # Rectangle with class methods
├── 101-nqueens.py       # N Queens problem solver
├── 0-main.py           # Test file for task 0
├── 1-main.py           # Test file for task 1
├── 2-main.py           # Test file for task 2
├── 3-main.py           # Test file for task 3
├── 4-main.py           # Test file for task 4
├── 5-main.py           # Test file for task 5
├── 6-main.py           # Test file for task 6
├── 7-main.py           # Test file for task 7
├── 8-main.py           # Test file for task 8
├── 9-main.py           # Test file for task 9
└── README.md           # This file
```

## Tasks

### 0. Simple rectangle
**File:** `0-rectangle.py`

Write an empty class `Rectangle` that defines a rectangle.

**Requirements:**
- You are not allowed to import any module

### 1. Real definition of a rectangle
**File:** `1-rectangle.py`

Write a class `Rectangle` that defines a rectangle by width and height attributes.

**Requirements:**
- Private instance attribute: `width` and `height`
- Property getters and setters for both attributes
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Width and height must be integers and >= 0
- You are not allowed to import any module

### 2. Area and Perimeter
**File:** `2-rectangle.py`

Write a class `Rectangle` that defines a rectangle with area and perimeter methods.

**Requirements:**
- Previous requirements
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter
- If width or height is 0, perimeter is 0
- You are not allowed to import any module

### 3. String representation
**File:** `3-rectangle.py`

Write a class `Rectangle` that defines a rectangle with string representation.

**Requirements:**
- Previous requirements
- `print()` and `str()` should print the rectangle with the character `#`
- If width or height is 0, return an empty string
- You are not allowed to import any module

### 4. Eval is magic
**File:** `4-rectangle.py`

Write a class `Rectangle` that defines a rectangle with both `__str__` and `__repr__` methods.

**Requirements:**
- Previous requirements
- `repr()` should return a string representation that can be used to recreate a new instance
- You are not allowed to import any module

### 5. Detect instance deletion
**File:** `5-rectangle.py`

Write a class `Rectangle` that defines a rectangle with deletion detection.

**Requirements:**
- Previous requirements
- Print the message "Bye rectangle..." when an instance is deleted
- You are not allowed to import any module

### 6. How many instances
**File:** `6-rectangle.py`

Write a class `Rectangle` that defines a rectangle with instance counting.

**Requirements:**
- Previous requirements
- Class attribute `number_of_instances`
- Incremented during each new instance instantiation
- Decremented during each instance deletion
- You are not allowed to import any module

### 7. Change representation
**File:** `7-rectangle.py`

Write a class `Rectangle` that defines a rectangle with customizable print symbol.

**Requirements:**
- Previous requirements
- Class attribute `print_symbol = "#"`
- Used as symbol for string representation
- Can be any type
- You are not allowed to import any module

### 8. Compare rectangles
**File:** `8-rectangle.py`

Write a class `Rectangle` that defines a rectangle with comparison method.

**Requirements:**
- Previous requirements
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on area
- If both have the same area value, return `rect_1`
- `rect_1` and `rect_2` must be instances of Rectangle, otherwise raise a TypeError
- You are not allowed to import any module

### 9. A square is a rectangle
**File:** `9-rectangle.py`

Write a class `Rectangle` that defines a rectangle with a class method to create squares.

**Requirements:**
- Previous requirements
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with width == height == size
- You are not allowed to import any module

### 10. N Queens (Advanced)
**File:** `101-nqueens.py`

Solve the N Queens puzzle - place N non-attacking queens on an N×N chessboard.

**Requirements:**
- Usage: `nqueens N`
- N must be an integer >= 4
- Print all possible solutions
- One solution per line
- Format: list of lists, each containing [row, column] of queen positions
- You are only allowed to import the sys module

## Usage Examples

### Basic Rectangle Usage
```python
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
```

### String Representation
```python
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))
```

### Instance Counting
```python
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
```

### Custom Print Symbol
```python
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)

print("--")

my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)

print("--")

Rectangle.print_symbol = "C"
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
```

### Rectangle Comparison
```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
```

### Creating Squares
```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
```

### N Queens Problem
```bash
./101-nqueens.py 4
# Output:
# [[0, 1], [1, 3], [2, 0], [3, 2]]
# [[0, 2], [1, 0], [2, 3], [3, 1]]

./101-nqueens.py 6
# Output: All possible solutions for 6x6 board
```

## Testing

Each task includes a corresponding main file for testing:

```bash
# Test each task
./0-main.py
./1-main.py
./2-main.py
# ... and so on

# Test N Queens
./101-nqueens.py 4
./101-nqueens.py 8
```

## Key Concepts Demonstrated

### Class vs Instance Attributes
- **Instance attributes**: Belong to specific instances (`self.width`, `self.height`)
- **Class attributes**: Shared by all instances (`Rectangle.number_of_instances`)

### Special Methods
- `__init__`: Constructor method
- `__str__`: Human-readable string representation
- `__repr__`: Unambiguous string representation for developers
- `__del__`: Destructor method called when object is deleted

### Method Types
- **Instance methods**: Operate on instance data (`area`, `perimeter`)
- **Class methods**: Operate on class data (`@classmethod`, `square`)
- **Static methods**: Independent utility functions (`@staticmethod`, `bigger_or_equal`)

### Properties
- Getter and setter methods using `@property` decorator
- Data validation and encapsulation

## Error Handling

The Rectangle class includes proper error handling:
- Type validation for width and height
- Value validation (non-negative numbers)
- TypeError exceptions for invalid rectangle comparisons

## Author

This project is part of the ALX Higher Level Programming curriculum, focusing on advanced Python OOP concepts.

## License

This project is part of the ALX curriculum and is intended for educational purposes.
