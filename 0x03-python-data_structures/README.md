# 0x03. Python - Data Structures: Lists, Tuples

## Description
This project focuses on understanding and working with Python's built-in data structures, specifically lists and tuples. You'll learn how to manipulate these data structures, understand their differences, and implement various operations and algorithms using them.

## Learning Objectives
At the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*) style
- All your files must be executable
- The length of your files will be tested using `wc`

### C
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=c89`
- All your files should end with a new line
- Your code should use the Betty style
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called `lists.h`
- All your header files should be include guarded

## Data Structures

### Lists
Lists are ordered, mutable collections that can contain items of different data types.

**Key characteristics:**
- Mutable (can be changed after creation)
- Ordered (items have a defined order)
- Allow duplicates
- Can contain different data types

**Common operations:**
```python
# Creating lists
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# Accessing elements
first_item = my_list[0]
last_item = my_list[-1]

# Modifying lists
my_list.append(6)
my_list.insert(0, 0)
my_list.remove(3)
my_list.pop()

# List slicing
subset = my_list[1:4]
```

### Tuples
Tuples are ordered, immutable collections.

**Key characteristics:**
- Immutable (cannot be changed after creation)
- Ordered (items have a defined order)
- Allow duplicates
- Can contain different data types
- Use parentheses `()` or just commas

**Common operations:**
```python
# Creating tuples
my_tuple = (1, 2, 3, 4, 5)
mixed_tuple = 1, "hello", 3.14, True

# Accessing elements
first_item = my_tuple[0]
last_item = my_tuple[-1]

# Tuple unpacking
a, b, c = (1, 2, 3)
```

## Project Tasks

The tasks in this project typically include:

1. **Print a list of integers** - Create a function that prints all integers in a list
2. **Secure access to an element** - Access list elements safely without causing errors
3. **Replace element** - Replace an element in a list at a specific position
4. **Print reversed list** - Print all integers of a list in reverse order
5. **Replace in a copy** - Replace elements without modifying the original list
6. **Remove characters** - Remove specific characters from strings
7. **Lists of lists = Matrix** - Work with matrices (lists of lists)
8. **Tuples addition** - Add corresponding elements from two tuples
9. **More returns** - Return multiple values using tuples
10. **Find the max** - Find the biggest integer in a list
11. **Only by 2** - Find multiples of 2 in a list
12. **Delete at** - Delete an item at a specific position
13. **Switch** - Switch values of two variables

## Usage Examples

### Working with Lists
```python
#!/usr/bin/python3
# Example: Print list elements
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

# Usage
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```

### Working with Tuples
```python
#!/usr/bin/python3
# Example: Multiple return values
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

# Usage
length, first = multiple_returns("Hello")
print("Length: {} - First character: {}".format(length, first))
```

## Key Concepts

### List Comprehensions
A concise way to create lists:
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]
```

### Sequence Unpacking
```python
# Tuple unpacking
coordinates = (3, 5)
x, y = coordinates

# List unpacking
numbers = [1, 2, 3]
a, b, c = numbers
```

### Using Lists as Stacks and Queues
```python
# Stack (LIFO - Last In, First Out)
stack = [1, 2, 3]
stack.append(4)  # Push
item = stack.pop()  # Pop

# Queue (FIFO - First In, First Out)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # Enqueue
item = queue.popleft()  # Dequeue
```

## Files Structure
```
0x03-python-data_structures/
├── README.md
├── 0-print_list_integer.py
├── 1-element_at.py
├── 2-replace_in_list.py
├── 3-print_reversed_list_integer.py
├── 4-new_in_list.py
├── 5-no_c.py
├── 6-print_matrix_integer.py
├── 7-add_tuple.py
├── 8-multiple_returns.py
├── 9-max_integer.py
├── 10-divisible_by_2.py
├── 11-delete_at.py
├── 12-switch.py
├── 13-is_palindrome.c
├── lists.h
└── test files...
```

## Testing
Each function should be tested with various inputs:
```bash
# Run individual test files
python3 0-main.py
python3 1-main.py

# Compile C files
gcc -Wall -Werror -Wextra -pedantic -std=c89 13-main.c 13-is_palindrome.c -o palindrome
```

## Resources
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Author
This project is part of the ALX Software Engineering Program.

---
**Note:** Remember to always handle edge cases like empty lists, invalid indices, and None values in your implementations.