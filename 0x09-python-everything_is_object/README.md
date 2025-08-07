# 0x09. Python - Everything is object

This project explores one of Python's fundamental concepts: "Everything is an object". Through a series of questions and practical exercises, you'll deepen your understanding of how Python handles objects, references, mutability, and memory management.

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let's pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```python
>>> a = 1
>>> b = a
>>> a = 2
>>> print(b)
1
>>> 
```

OK. But what about this?

```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> print(m)
['x', 2, 3]
>>> 
```

This project will help you understand why this happens.

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

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

### .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## Files Description

### Answer Files

| File | Question | Topic |
|------|----------|-------|
| `0-answer.txt` | What function would you use to get the type of an object? | Type function |
| `1-answer.txt` | How do you get the variable identifier? | Memory address |
| `2-answer.txt` | Do `a` and `b` point to the same object? | Object identity |
| `3-answer.txt` | Do `a` and `b` point to the same object? | Object identity |
| `4-answer.txt` | Do `a` and `b` point to the same object? | Object identity |
| `5-answer.txt` | Do `a` and `b` point to the same object? | Object identity |
| `6-answer.txt` | What do these 3 lines print? | Variable comparison |
| `7-answer.txt` | What do these 3 lines print? | Variable comparison |
| `8-answer.txt` | What do these 3 lines print? | Variable comparison |
| `9-answer.txt` | What do these 3 lines print? | Variable comparison |
| `10-answer.txt` | What do these 3 lines print? | List comparison |
| `11-answer.txt` | What do these 3 lines print? | List comparison |
| `12-answer.txt` | What do these 3 lines print? | List comparison |
| `13-answer.txt` | What do these 3 lines print? | List comparison |
| `14-answer.txt` | What does this script print? | List operations |
| `15-answer.txt` | What does this script print? | List operations |
| `16-answer.txt` | What does this script print? | Integer increment |
| `17-answer.txt` | What does this script print? | List operations |
| `18-answer.txt` | What does this script print? | List operations |
| `20-answer.txt` | Is `a` a tuple? | Tuple syntax |
| `21-answer.txt` | Is `a` a tuple? | Tuple syntax |
| `22-answer.txt` | Is `a` a tuple? | Tuple syntax |
| `23-answer.txt` | Is `a` a tuple? | Tuple syntax |
| `24-answer.txt` | What does this script print? | Tuple mutability |
| `25-answer.txt` | What does this script print? | Tuple operations |
| `26-answer.txt` | What does this script print? | Tuple identity |
| `27-answer.txt` | Will the last line print 139926795932424? | ID behavior |
| `28-answer.txt` | Will the last line print 139926795932424? | ID behavior |

### Python Files

| File | Description |
|------|-------------|
| `19-copy_list.py` | Function that returns a copy of a list |
| `19-main.py` | Test file for the copy_list function |

## Tasks

### 0. Who am I?
**File**: `0-answer.txt`

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.

### 1. Where are you?
**File**: `1-answer.txt`

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

### 2. Right count
**File**: `2-answer.txt`

In the following code, do `a` and `b` point to the same object?
Answer with `Yes` or `No`.

```python
>>> a = 89
>>> b = 100
```

### 3. Right count =
**File**: `3-answer.txt`

In the following code, do `a` and `b` point to the same object?
Answer with `Yes` or `No`.

```python
>>> a = 89
>>> b = 89
```

### 4. Right count =
**File**: `4-answer.txt`

In the following code, do `a` and `b` point to the same object?
Answer with `Yes` or `No`.

```python
>>> a = 89
>>> b = a
```

### 5. Right count =+
**File**: `5-answer.txt`

In the following code, do `a` and `b` point to the same object?
Answer with `Yes` or `No`.

```python
>>> a = 89
>>> b = a + 1
```

### 19. Copy a list object
**File**: `19-copy_list.py`

Write a function `def copy_list(l):` that returns a copy of a list.

**Requirements**:
- The input list can contain any type of objects
- Your file should be maximum 3 lines long (no documentation needed)
- You are not allowed to import any module

## Key Concepts Covered

### Object Identity vs Equality
- `is` vs `==` operators
- When Python creates new objects vs reuses existing ones
- Small integer caching (-5 to 256)
- String interning

### Mutable vs Immutable Objects

**Immutable Types**:
- int, float, complex
- str
- tuple
- frozenset
- bool

**Mutable Types**:
- list
- dict
- set
- Custom objects (usually)

### Memory Management
- Object references and aliases
- When objects are created vs reused
- The `id()` function and memory addresses
- Garbage collection concepts

### Function Parameter Passing
- Pass by object reference
- How mutable and immutable objects behave when passed to functions
- The difference between modifying an object vs reassigning a variable

## Usage Examples

### Checking Object Identity
```python
>>> a = [1, 2, 3]
>>> b = a
>>> c = a[:]
>>> print(a is b)        # Same object
>>> print(a is c)        # Different objects
>>> print(a == c)        # Same content
```

### Integer Caching
```python
>>> a = 256
>>> b = 256
>>> print(a is b)        # True (cached)
>>> a = 257
>>> b = 257
>>> print(a is b)        # May be False (not cached)
```

### List Copying
```python
from copy_list import copy_list

original = [1, 2, 3]
copied = copy_list(original)
print(original is copied)    # False
print(original == copied)    # True
```

## Testing

To test your understanding, try running the Python interpreter and experimenting with:

```python
# Object identity
>>> a = 89
>>> b = 89
>>> print(id(a))
>>> print(id(b))
>>> print(a is b)

# Mutable objects
>>> list1 = [1, 2, 3]
>>> list2 = list1
>>> list1.append(4)
>>> print(list2)

# Immutable objects
>>> str1 = "Hello"
>>> str2 = str1
>>> str1 += " World"
>>> print(str2)
```

## Author
This project is part of the ALX Higher Level Programming curriculum.

## Resources
- [9.10. Objects and values](https://docs.python.org/3/tutorial/classes.html#objects-and-values)
- [9.11. Aliasing](https://docs.python.org/3/tutorial/classes.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html#sequence-objects)
- [9.12. Cloning lists](https://docs.python.org/3/tutorial/classes.html#cloning-lists)
- [Python tuples: immutable but potentially changing](https://stackoverflow.com/questions/9755990/python-tuples-immutable-but-potentially-changing)
