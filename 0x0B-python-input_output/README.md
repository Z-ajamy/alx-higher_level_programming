# 0x0B. Python - Input/Output

This project explores file handling and JSON manipulation in Python. You'll learn how to read and write files, work with JSON data, serialize and deserialize Python objects, and handle various input/output operations effectively.

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

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

### Implementation Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Function that reads a text file (UTF8) and prints it to stdout |
| `1-write_file.py` | Function that writes a string to a text file (UTF8) and returns the number of characters written |
| `2-append_write.py` | Function that appends a string at the end of a text file (UTF8) and returns the number of characters added |
| `3-to_json_string.py` | Function that returns the JSON representation of an object (string) |
| `4-from_json_string.py` | Function that returns an object (Python data structure) represented by a JSON string |
| `5-save_to_json_file.py` | Function that writes an Object to a text file, using a JSON representation |
| `6-load_from_json_file.py` | Function that creates an Object from a "JSON file" |
| `7-add_item.py` | Script that adds all arguments to a Python list, and then save them to a file |
| `8-class_to_json.py` | Function that returns the dictionary description with simple data structure for JSON serialization of an object |
| `9-student.py` | Class Student that defines a student by first_name, last_name and age |
| `10-student.py` | Class Student with method to retrieve dictionary representation |
| `11-student.py` | Class Student with method to replace all attributes from JSON dictionary |

### Test Files

| File | Description |
|------|-------------|
| `0-main.py` | Test file for read_file function |
| `1-main.py` | Test file for write_file function |
| `2-main.py` | Test file for append_write function |
| `3-main.py` | Test file for to_json_string function |
| `4-main.py` | Test file for from_json_string function |
| `5-main.py` | Test file for save_to_json_file function |
| `6-main.py` | Test file for load_from_json_file function |
| `8-main_2.py` | Test file for class_to_json function |
| `8-my_class.py` | Example class for testing class_to_json |
| `9-main.py` | Test file for Student class |
| `10-main.py` | Test file for improved Student class |
| `11-main.py` | Test file for final Student class |

### Generated Files

| File | Description |
|------|-------------|
| `add_item.json` | JSON file created by add_item.py script |

## Tasks

### 0. Read file
**File**: `0-read_file.py`

Write a function that reads a text file (UTF8) and prints it to stdout.

**Prototype**: `def read_file(filename=""):`
**Requirements**:
- You must use the `with` statement
- You don't need to manage `file` permission or `file` doesn't exist exceptions
- You are not allowed to import any module

### 1. Write to a file
**File**: `1-write_file.py`

Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

**Prototype**: `def write_file(filename="", text=""):`
**Requirements**:
- You must use the `with` statement
- You don't need to manage file permission exceptions
- Your function should create the file if it doesn't exist
- Your function should overwrite the content of the file if it already exists
- You are not allowed to import any module

### 2. Append to a file
**File**: `2-append_write.py`

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

**Prototype**: `def append_write(filename="", text=""):`
**Requirements**:
- If the file doesn't exist, it should be created
- You must use the `with` statement
- You don't need to manage file permission or file doesn't exist exceptions
- You are not allowed to import any module

### 3. To JSON string
**File**: `3-to_json_string.py`

Write a function that returns the JSON representation of an object (string).

**Prototype**: `def to_json_string(my_obj):`
**Requirements**:
- You don't need to manage exceptions if the object can't be serialized

### 4. From JSON string to Object
**File**: `4-from_json_string.py`

Write a function that returns an object (Python data structure) represented by a JSON string.

**Prototype**: `def from_json_string(my_str):`
**Requirements**:
- You don't need to manage exceptions if the JSON string doesn't represent an object

### 5. Save Object to a file
**File**: `5-save_to_json_file.py`

Write a function that writes an Object to a text file, using a JSON representation.

**Prototype**: `def save_to_json_file(my_obj, filename):`
**Requirements**:
- You must use the `with` statement
- You don't need to manage exceptions if the object can't be serialized
- You don't need to manage file permission exceptions

### 6. Create object from a JSON file
**File**: `6-load_from_json_file.py`

Write a function that creates an Object from a "JSON file".

**Prototype**: `def load_from_json_file(filename):`
**Requirements**:
- You must use the `with` statement
- You don't need to manage exceptions if the JSON string doesn't represent an object
- You don't need to manage file permissions / exceptions

### 7. Load, add, save
**File**: `7-add_item.py`

Write a script that adds all arguments to a Python list, and then save them to a file.

**Requirements**:
- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn't exist, it should be created
- You don't need to manage file permissions / exceptions

### 8. Class to JSON
**File**: `8-class_to_json.py`

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

**Prototype**: `def class_to_json(obj):`
**Requirements**:
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

### 9. Student to JSON
**File**: `9-student.py`

Write a class `Student` that defines a student by:

**Requirements**:
- Public instance attributes: `first_name`, `last_name` and `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
- You are not allowed to import any module

### 10. Student to JSON with filter
**File**: `10-student.py`

Write a class `Student` that defines a student by: (based on `9-student.py`)

**Requirements**:
- Public instance attributes: `first_name`, `last_name` and `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance
- If `attrs` is a list of strings, only attribute names contained in this list must be retrieved
- Otherwise, all attributes must be retrieved
- You are not allowed to import any module

### 11. Student to disk and reload
**File**: `11-student.py`

Write a class `Student` that defines a student by: (based on `10-student.py`)

**Requirements**:
- Public instance attributes: `first_name`, `last_name` and `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance
- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance
- You can assume `json` will always be a dictionary
- A dictionary key will be the public attribute name
- A dictionary value will be the value of the public attribute
- You are not allowed to import any module

## Key Concepts

### File Operations

**Reading Files**:
```python
# Method 1: Using with statement (recommended)
with open('filename.txt', 'r') as file:
    content = file.read()

# Method 2: Reading line by line
with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

**Writing Files**:
```python
# Writing (overwrites existing content)
with open('filename.txt', 'w') as file:
    file.write('Hello, World!')

# Appending (adds to existing content)
with open('filename.txt', 'a') as file:
    file.write('Additional content')
```

### JSON Operations

**Serialization (Python to JSON)**:
```python
import json

data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)  # Convert to JSON string
```

**Deserialization (JSON to Python)**:
```python
import json

json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)  # Convert to Python object
```

**File Operations with JSON**:
```python
import json

# Save to file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Load from file
with open('data.json', 'r') as file:
    data = json.load(file)
```

### Class Serialization

Objects can be serialized by converting their `__dict__` attribute:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def to_json(self):
        return self.__dict__
```

## Usage Examples

### Basic File Operations
```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
```

### JSON Operations
```python
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s = to_json_string(my_list)
print(s)
print(type(s))
```

### Student Class Usage
```python
#!/usr/bin/python3
Student = __import__('11-student').Student

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()

student_2 = Student("Bob", "Dylan", 27)
j_student_2 = student_2.to_json(['first_name', 'age'])

print(j_student_1)
print(j_student_2)
```

### Command Line Script
```bash
# Using add_item.py
./7-add_item.py "Best" "School" "89" "Python C"
# Creates/updates add_item.json with the arguments
```

## File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read mode (default) |
| `'w'` | Write mode (overwrites existing file) |
| `'a'` | Append mode (adds to end of file) |
| `'x'` | Exclusive creation mode (fails if file exists) |
| `'b'` | Binary mode |
| `'t'` | Text mode (default) |
| `'+'` | Read and write mode |

## Error Handling

While not required for this project, proper error handling in production code:

```python
try:
    with open('filename.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except IOError:
    print("IO error occurred")
```

## JSON Data Types

JSON supports the following data types:
- **String**: Text in double quotes
- **Number**: Integer or floating point
- **Boolean**: true or false
- **null**: Represents empty value
- **Object**: Collection of key-value pairs in curly braces
- **Array**: Ordered list of values in square brackets

## Testing

### Manual Testing
```bash
python3 0-main.py
python3 1-main.py
# ... and so on for each main file
```

### Testing with Arguments
```bash
python3 7-add_item.py "Hello" "World" "89" "Best School"
cat add_item.json
```

### Checking Documentation
```bash
python3 -c 'print(__import__("1-write_file").__doc__)'
python3 -c 'print(__import__("1-write_file").write_file.__doc__)'
```

## Best Practices

1. **Always use `with` statement** for file operations to ensure proper cleanup
2. **Handle exceptions** appropriately in production code
3. **Use UTF-8 encoding** for text files to support international characters
4. **Validate JSON data** before processing in production applications
5. **Use meaningful variable names** and add docstrings to functions
6. **Close files properly** (automatically handled by `with` statement)

## Author
This project is part of the ALX Higher Level Programming curriculum.

## Resources
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](http://www.diveintopython3.net/files.html)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)