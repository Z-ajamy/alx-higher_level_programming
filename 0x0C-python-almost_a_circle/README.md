# 0x0C. Python - Almost a circle

This project is a comprehensive review of Python Object-Oriented Programming concepts. You'll implement a complete application using classes, inheritance, serialization, and unit testing. The project simulates a graphics library with geometric shapes, focusing on rectangles and squares.

## Background Context

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:
- `*args` and `**kwargs`
- Serialization/Deserialization
- JSON

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

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
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_method.__doc__)'`

### Python Unit Tests
- All your test files should be inside a folder `tests`
- You have to use the unittest module
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- All your modules should be documented
- All your classes should be documented
- All your functions (inside and outside a class) should be documented

## Project Structure

```
0x0C-python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   └── test_models/
│       ├── __init__.py
│       ├── test_base.py
│       ├── test_rectangle.py
│       └── test_square.py
├── main files (0-main.py to 13-main.py)
└── README.md
```

## Files Description

### Model Files

| File | Description |
|------|-------------|
| `models/__init__.py` | Makes models a Python package |
| `models/base.py` | Base class that manages id attribute and JSON serialization |
| `models/rectangle.py` | Rectangle class that inherits from Base |
| `models/square.py` | Square class that inherits from Rectangle |

### Test Files

| Directory/File | Description |
|----------------|-------------|
| `tests/` | Directory containing all unit tests |
| `tests/test_models/` | Directory containing model tests |
| `tests/test_models/__init__.py` | Makes test_models a Python package |
| `tests/test_models/test_base.py` | Unit tests for Base class |
| `tests/test_models/test_rectangle.py` | Unit tests for Rectangle class |
| `tests/test_models/test_square.py` | Unit tests for Square class |

### Main Test Files

| File | Description |
|------|-------------|
| `0-main.py` | Test Base class instantiation |
| `1-main.py` | Test Rectangle class instantiation |
| `2-main.py` | Test Rectangle validation |
| `3-main.py` | Test Rectangle area calculation |
| `4-main.py` | Test Rectangle display method |
| `5-main.py` | Test Rectangle string representation |
| `6-main.py` | Test Rectangle display with position |
| `7-main.py` | Test Rectangle update method with *args |
| `8-main.py` | Test Rectangle update method with **kwargs |
| `9-main.py` | Test Square class |
| `10-main.py` | Test Square size getter/setter |
| `11-main.py` | Test Square update method |
| `12-main.py` | Test Rectangle to_dictionary method |
| `13-main.py` | Test Square to_dictionary method |

## Tasks Overview

### 0. If it's not tested it doesn't work
Write the first class `Base` with:
- Private class attribute `__nb_objects = 0`
- Class constructor: `def __init__(self, id=None):`
- If `id` is not `None`, assign the public instance attribute `id` with this argument value
- Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

### 1. Base class
Write the class `Rectangle` that inherits from `Base`:
- Private instance attributes, each with its own public getter and setter:
  - `__width` -> `width`
  - `__height` -> `height`
  - `__x` -> `x`
  - `__y` -> `y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`

### 2. Validate attributes
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):
- If the input is not an integer, raise a `TypeError` exception with the message: `<name of the attribute> must be an integer`
- If `width` or `height` is under or equals 0, raise a `ValueError` exception with the message: `<name of the attribute> must be > 0`
- If `x` or `y` is under 0, raise a `ValueError` exception with the message: `<name of the attribute> must be >= 0`

### 3. Area first
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the Rectangle instance.

### 4. Display #0
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the Rectangle instance with the character `#` - you don't need to handle `x` and `y` here.

### 5. __str__
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

### 6. Display #1
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the Rectangle instance with the character `#` by taking care of `x` and `y`

### 7. Update #0
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:
- 1st argument should be the `id` attribute
- 2nd argument should be the `width` attribute
- 3rd argument should be the `height` attribute
- 4th argument should be the `x` attribute
- 5th argument should be the `y` attribute

### 8. Update #1
Update the class `Rectangle` by updating the public method `def update(self, *args, **kwargs):` that assigns a key/value argument to attributes:
- `**kwargs` can be thought of as a double pointer to a dictionary: key/value
- As Python doesn't have pointers, `**kwargs` is not literally a double pointer – describing it this way will help you understand it
- `**kwargs` must be skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance

### 9. And now, the Square!
Write the class `Square` that inherits from `Rectangle`:
- Class constructor: `def __init__(self, size, x=0, y=0, id=None):`
- The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>`
- The `width` and `height` must be assigned to the value of `size`
- You must use the `super()` method

### 10. Square size
Update the class `Square` by adding the public getter and setter `size`:
- The setter should assign (in this order) the `width` and the `height` - with the same value
- The setter should have the same validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`)

### 11. Square update
Update the class `Square` by adding the public method `def update(self, *args, **kwargs):` that assigns attributes:
- `*args` is the list of arguments - no-keyworded arguments
  - 1st argument should be the `id` attribute
  - 2nd argument should be the `size` attribute
  - 3rd argument should be the `x` attribute
  - 4th argument should be the `y` attribute
- `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
- `**kwargs` must be skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance

### 12. Rectangle instance to dictionary representation
Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle:
This dictionary must contain:
- `id`
- `width`
- `height`
- `x`
- `y`

### 13. Square instance to dictionary representation
Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Square:
This dictionary must contain:
- `id`
- `size`
- `x`
- `y`

### 14. Dictionary to JSON string
JSON is one of the standard formats for sharing data representation.

Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`:
- `list_dictionaries` is a list of dictionaries
- If `list_dictionaries` is `None` or empty, return the string: `"[]"`
- Otherwise, return the JSON string representation of `list_dictionaries`

### 15. JSON string to file
Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file:
- `list_objs` is a list of instances who inherits of `Base` - example: list of `Rectangle` or list of `Square` instances
- If `list_objs` is `None`, save an empty list
- The filename must be: `<Class name>.json` - example: `Rectangle.json`
- You must use the static method `to_json_string` (created before)
- You must overwrite the file if it already exists

### 16. JSON string to dictionary
Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`:
- `json_string` is a string representing a list of dictionaries
- If `json_string` is `None` or empty, return an empty list
- Otherwise, return the list represented by `json_string`

### 17. Dictionary to Instance
Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set:
- `**dictionary` can be thought of as a double pointer to a dictionary
- To use the update method to assign all attributes, you must create a "dummy" instance before:
  - Create a Rectangle or Square instance with "dummy" mandatory attributes (width, height, size, etc.)
  - Call `update` instance method to this "dummy" instance to apply your real values
- You must use the method `update` from task 8 or 11
- `**dictionary` must be used as `**kwargs` of the method `update`
- You are not allowed to use `eval`

### 18. File to instances
Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances:
- The filename must be: `<Class name>.json` - example: `Rectangle.json`
- If the file doesn't exist, return an empty list
- Otherwise, return a list of instances - the type of these instances depends on `cls` (current class using this method)
- You must use the `from_json_string` and `create` methods (implemented previously)

## Class Hierarchy

```
Base
 └── Rectangle
      └── Square
```

## Key Concepts Implemented

### Object-Oriented Programming
- **Inheritance**: Square inherits from Rectangle, Rectangle inherits from Base
- **Encapsulation**: Private attributes with public getters/setters
- **Polymorphism**: Method overriding (__str__, update methods)

### Advanced Python Features
- **`*args`**: Variable number of positional arguments
- **`**kwargs`**: Variable number of keyword arguments
- **Static methods**: Methods that don't need instance or class state
- **Class methods**: Methods that work with class state

### Serialization
- **JSON**: Converting Python objects to JSON strings and vice versa
- **File I/O**: Reading and writing JSON data to files
- **Dictionary representation**: Converting objects to dictionaries

## Usage Examples

### Basic Usage
```python
#!/usr/bin/python3
"""Test Base class"""
from models.base import Base

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
```

### Rectangle Operations
```python
#!/usr/bin/python3
"""Test Rectangle"""
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
```

### Square Operations
```python
#!/usr/bin/python3
"""Test Square"""
from models.square import Square

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()
```

### JSON Serialization
```python
#!/usr/bin/python3
"""Test JSON serialization"""
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Rectangle.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
```

## Testing

### Running All Tests
```bash
python3 -m unittest discover tests
```

### Running Specific Test Files
```bash
python3 -m unittest tests/test_models/test_base.py
python3 -m unittest tests/test_models/test_rectangle.py
python3 -m unittest tests/test_models/test_square.py
```

### Running Individual Test Methods
```bash
python3 -m unittest tests.test_models.test_rectangle.TestRectangle.test_area
```

### Test Coverage
The tests should cover:
- **Positive cases**: Normal functionality
- **Edge cases**: Boundary values, empty inputs
- **Error cases**: Invalid inputs, type errors, value errors
- **Method behavior**: All public methods and their expected outputs

## Error Handling

The implementation includes comprehensive validation:

```python
# Type validation
if not isinstance(value, int):
    raise TypeError("{} must be an integer".format(name))

# Value validation
if value <= 0:  # for width and height
    raise ValueError("{} must be > 0".format(name))

if value < 0:   # for x and y
    raise ValueError("{} must be >= 0".format(name))
```

## File Structure Best Practices

- **Modular design**: Separate classes in different files
- **Package structure**: Proper `__init__.py` files
- **Test organization**: Mirror the main code structure in tests
- **Documentation**: Comprehensive docstrings for all modules, classes, and methods

## Author
This project is part of the ALX Higher Level Programming curriculum.

## Resources
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest — Unit testing framework](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [Object Oriented Programming](https://python.swaroopch.com/oop.html)
