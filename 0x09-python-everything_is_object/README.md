# 0x09. Python — Everything is an Object

## Table of Contents

- [Project Overview](#project-overview)  
- [Learning Objectives](#learning-objectives)  
- [Key Concepts](#key-concepts)  
  - [Objects in Python](#objects-in-python)  
  - [Identity, Type, and Value](#identity-type-and-value)  
  - [Mutable vs Immutable Objects](#mutable-vs-immutable-objects)  
  - [Aliasing and References](#aliasing-and-references)  
  - [Passing Objects to Functions](#passing-objects-to-functions)  
- [Learning Resources](#learning-resources)  
- [Project Structure](#project-structure)  
- [Usage Instructions](#usage-instructions)  
- [Why This Matters](#why-this-matters)  
- [Author](#author)

---

## Project Overview

This repository is part of the **ALX Higher Level Programming** curriculum, specifically the section focused on reinforcing the concept that **“everything in Python is an object.”**  
Here, you will explore how Python handles variables, objects, memory, and references behind the scenes, solidifying your understanding of object identity, mutability, aliasing, and behavior when using built-in data types and custom code constructs.

---

## Learning Objectives

By completing this project, you will:

1. Understand the core principle: **everything is an object** in Python—data types, functions, classes, and modules alike.  
2. Differentiate between **mutable** and **immutable** objects, with real examples and practical implications.  
3. Use and interpret `id()`, `type()`, and the `is` operator to probe object identity and behavior at runtime.  
4. Recognize how aliasing can lead to shared references and unexpected side-effects in mutable objects.  
5. Grasp the behavior of passing mutable and immutable objects to functions, especially regarding changes to data inside functions.  
6. Appreciate the role of object-oriented features such as attributes and methods on all object types.

---

## Key Concepts

### Objects in Python

In Python, everything you can assign to a variable—or pass as an argument—is an object. Whether it's an integer (`1`), a string (`"hello"`), a list `[1, 2, 3]`, a function, or even a module—each is treated as an object, complete with metadata and behavior. For example, functions have attributes like `__doc__`, and modules are treated as mutable objects where you can dynamically add attributes :contentReference[oaicite:0]{index=0}.

Furthermore, the concept of metaclasses means that even classes themselves are objects—instances of `type`—allowing deep-level introspection and dynamic behavior :contentReference[oaicite:1]{index=1}.

---

### Identity, Type, and Value

Every object in Python has:

- **Identity**: A unique memory address returned by `id()`.  
- **Type**: Indicates the class to which the object belongs, accessible via `type()`.  
- **Value**: The actual data or content that the object holds.

```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # e.g., 140703548773520

Author
This project is part of the ALX Higher Level Programming curriculum, focusing on Python classes and object-oriented programming concepts.
License
This project is part of the ALX curriculum and is intended for educational purposes.

## Author

This project is part of the ALX Higher Level Programming curriculum, focusing on Python classes and object-oriented programming concepts.

## License

This project is part of the ALX curriculum and is intended for educational purposes.
