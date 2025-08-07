# 0x0A. Python - Inheritance

This project explores one of the fundamental concepts of Object-Oriented Programming: Inheritance. You'll learn how to create class hierarchies, override methods, use built-in functions to inspect class relationships, and implement proper inheritance patterns in Python.

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by inheritance to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

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
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_method.__doc__)'`)

## Files Description

### Main Implementation Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Function that returns the list of available attributes and methods of an object |
| `1-my_list.py` | Class MyList that inherits from list |
| `2-is_same_class.py` | Function that returns True if object is exactly an instance of the specified class |
| `3-is_kind_of_class.py` | Function that returns True if object is an instance of, or inherited from, the specified class |
| `4-inherits_from.py` | Function that returns True if object is an instance of a class that inherited from the specified class |
| `5-base_geometry.py` | Empty class BaseGeometry |
| `6-base_geometry.py` | Class BaseGeometry with area method |
| `7-base_geometry.py` | Class BaseGeometry with area and integer_validator methods |
| `8-rectangle.py` | Class Rectangle that inherits from BaseGeometry |
| `9-rectangle.py` | Class Rectangle with area method implemented |
| `10-square.py` | Class Square that inherits from Rectangle |
| `11-square.py` | Class Square with improved string representation |

### Test Files

| File | Description |
|------|-------------|
| `0-main.py` | Test file for lookup function |
| `1-main.py` | Test file for MyList class |
| `2-main.py` | Test file for is_same_class function |
| `3-main.py` | Test file for is_kind_of_class function |
| `4-main.py` | Test file for inherits_from function |
| `5-main.py` | Test file for BaseGeometry (empty) |
| `6-main.py` | Test file for BaseGeometry with area method |
| `7-main.py` | Test file for BaseGeometry with validation |
| `8-main.py` | Test file for Rectangle class |
| `9-main.py` | Test file for Rectangle with area |
| `10-main.py` | Test file for Square class |
| `11-main.py` | Test file for improved Square class |

### Test Directory
- `tests/` - Directory containing doctests for various modules

## Tasks

### 0. Lookup
**File**: `0-lookup.py`

Write a function that returns the list of available attributes and methods of an object.

**Prototype**: `def lookup(obj):`
**Returns**: A list object
**You are not allowed to import any module**

### 1. My list
**File**: `1-my_list.py`

Write a class `MyList` that inherits from `list`.

**Requirements**:
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- You are not allowed to import any module

### 2. Exact same object
**File**: `2-is_same_class.py`

Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

**Prototype**: `def is_same_class(obj, a_class):`
**You are not allowed to import any module**

### 3. Same class or inherit from
**File**: `3-is_kind_of_class.py`

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

**Prototype**: `def is_kind_of_class(obj, a_class):`
**You are not allowed to import any module**

### 4. Only sub class of
**File**: `4-inherits_from.py`

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

**Prototype**: `def inherits_from(obj, a_class):`
**You are not allowed to import any module**

### 5. Geometry module
**File**: `5-base_geometry.py`

Write an empty class `BaseGeometry`.

**You are not allowed to import any module**

### 6. Improve Geometry
**File**: `6-base_geometry.py`

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

**Requirements**:
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- You are not allowed to import any module

### 7. Integer validator
**File**: `7-base_geometry.py`

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

**Requirements**:
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):` that validates `value`
  - You can assume `name` is always a string
  - If `value` is not an integer: raise a `TypeError` exception with the message `<name> must be an integer`
  - If `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
- You are not allowed to import any module

### 8. Rectangle
**File**: `8-rectangle.py`

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

**Requirements**:
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- `width` and `height` must be private. No getter or setter
- `width` and `height` must be positive integers, validated by `integer_validator`

### 9. Full rectangle
**File**: `9-rectangle.py`

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

**Requirements**:
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- `width` and `height` must be private. No getter or setter
- `width` and `height` must be positive integers, validated by `integer_validator`
- The `area()` method must be implemented
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

### 10. Square #1
**File**: `10-square.py`

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`).

**Requirements**:
- Instantiation with `size`: `def __init__(self, size):`
- `size` must be private. No getter or setter
- `size` must be a positive integer, validated by `integer_validator`
- The `area()` method must be implemented (it is already implemented in `Rectangle`)

### 11. Square #2
**File**: `11-square.py`

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`).

**Requirements**:
- Instantiation with `size`: `def __init__(self, size):`
- `size` must be private. No getter or setter
- `size` must be a positive integer, validated by `integer_validator`
- The `area()` method must be implemented (it is already implemented in `Rectangle`)
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

## Key Concepts

### Inheritance Hierarchy
```
BaseGeometry
    └── Rectangle
            └── Square
```

### Built-in Functions for Inheritance

**`isinstance(obj, class_or_tuple)`**
- Returns `True` if `obj` is an instance of `class_or_tuple` or any subclass thereof

**`issubclass(class, class_or_tuple)`**
- Returns `True` if `class` is a subclass of `class_or_tuple`

**`type(obj)`**
- Returns the exact type of `obj`

**`super()`**
- Returns a proxy object that allows access to methods in a parent class

### Method Resolution Order (MRO)
Python uses C3 linearization to determine the order in which base classes are searched when looking for a method.

## Usage Examples

### Basic Inheritance
```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)
print(r)
print(r.area())
```

### Class Inspection
```python
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
```

### Inheritance Checking
```python
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
```

### Square Usage
```python
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)
print(s)
print(s.area())
```

## Testing

### Running Doctests
```bash
python3 -m doctest ./tests/*
```

### Manual Testing
```bash
python3 0-main.py
python3 1-main.py
# ... and so on for each main file
```

### Checking Documentation
```bash
python3 -c 'print(__import__("1-my_list").__doc__)'
python3 -c 'print(__import__("1-my_list").MyList.__doc__)'
python3 -c 'print(__import__("1-my_list").MyList.print_sorted.__doc__)'
```

## Advanced Concepts

### Multiple Inheritance
While not directly used in this project, Python supports multiple inheritance:

```python
class A:
    pass

class B:
    pass

class C(A, B):  # Multiple inheritance
    pass
```

### Method Overriding
Subclasses can override methods from their parent classes:

```python
class Parent:
    def method(self):
        return "Parent method"

class Child(Parent):
    def method(self):  # Override
        return "Child method"
```

### Using super()
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
```

## Author
This project is part of the ALX Higher Level Programming curriculum.

## Resources
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://www.programiz.com/python-programming/inheritance)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
