# ALX Higher Level Programming: Python If/Else, Loops & Functions

## Overview

This module covers fundamental Python programming concepts including conditional statements, loops, and functions. These are essential building blocks for any Python program.

## Learning Objectives

By the end of this module, you should be able to:

- Use if, elif, and else statements for conditional execution
- Implement various types of loops (for, while)
- Create and use functions effectively
- Understand variable scope and function parameters
- Apply best practices for code organization and readability

## 1. Conditional Statements (If/Else)

### Basic If Statement

```python
if condition:
    # Code to execute if condition is True
    pass
```

### If-Else Statement

```python
if condition:
    # Code if condition is True
    pass
else:
    # Code if condition is False
    pass
```

### If-Elif-Else Statement

```python
if condition1:
    # Code if condition1 is True
    pass
elif condition2:
    # Code if condition2 is True
    pass
else:
    # Code if all conditions are False
    pass
```

### Practical Examples

```python
# Example 1: Age verification
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 2: Grade evaluation
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# Example 3: Multiple conditions
temperature = 25
weather = "sunny"
if temperature > 20 and weather == "sunny":
    print("Perfect day for a picnic!")
```

## 2. Loops

### For Loops

For loops are used to iterate over sequences (lists, tuples, strings, ranges).

```python
# Basic for loop with range
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# For loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# For loop with string
for char in "Hello":
    print(char)

# For loop with range parameters
for i in range(1, 10, 2):  # start, stop, step
    print(i)  # Prints 1, 3, 5, 7, 9
```

### While Loops

While loops continue executing as long as a condition is True.

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with user input
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
```

### Loop Control Statements

```python
# Break statement - exits the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue statement - skips current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints 1, 3, 5, 7, 9

# Else clause with loops
for i in range(5):
    print(i)
else:
    print("Loop completed normally")
```

### Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row
```

## 3. Functions

### Basic Function Definition

```python
def function_name():
    """Optional docstring"""
    # Function body
    pass

# Function call
function_name()
```

### Functions with Parameters

```python
def greet(name):
    """Greets a person with their name"""
    print(f"Hello, {name}!")

# Function call with argument
greet("Alice")

# Function with multiple parameters
def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

result = add_numbers(5, 3)
print(result)  # Prints 8
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    """Greets a person with a customizable greeting"""
    print(f"{greeting}, {name}!")

greet("Bob")  # Uses default greeting
greet("Bob", "Hi")  # Uses custom greeting
```

### Keyword Arguments

```python
def create_profile(name, age, city="Unknown"):
    """Creates a user profile"""
    return f"Name: {name}, Age: {age}, City: {city}"

# Different ways to call the function
profile1 = create_profile("Alice", 25)
profile2 = create_profile("Bob", age=30, city="New York")
profile3 = create_profile(city="Paris", name="Charlie", age=28)
```

### Variable-Length Arguments

```python
# *args for variable positional arguments
def sum_all(*numbers):
    """Returns the sum of all arguments"""
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # Prints 15

# **kwargs for variable keyword arguments
def print_info(**info):
    """Prints all keyword arguments"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Boston")
```

### Return Statements

```python
def calculate_area(length, width):
    """Calculates and returns the area of a rectangle"""
    area = length * width
    return area

def get_name_length(name):
    """Returns the length of a name"""
    return len(name)

def divide_numbers(a, b):
    """Divides two numbers with error handling"""
    if b == 0:
        return None  # Return None for division by zero
    return a / b

# Multiple return values
def get_name_parts(full_name):
    """Returns first and last name separately"""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]
    return parts[0], ""

first, last = get_name_parts("John Doe")
```

## 4. Variable Scope

### Local vs Global Variables

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

def another_function():
    # print(local_var)  # Error! Can't access local_var from my_function
    print(global_var)  # Can access global

# Using global keyword
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Prints 1
```

## 5. Best Practices and Common Patterns

### Input Validation

```python
def get_positive_number():
    """Gets a positive number from user input"""
    while True:
        try:
            num = float(input("Enter a positive number: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
```

### Menu-Driven Programs

```python
def display_menu():
    """Displays the main menu"""
    print("\n=== Main Menu ===")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("You selected Option 1")
        elif choice == "2":
            print("You selected Option 2")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### List Processing Functions

```python
def find_max(numbers):
    """Finds the maximum number in a list"""
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def filter_even(numbers):
    """Returns a list of even numbers"""
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def calculate_average(numbers):
    """Calculates the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

## 6. Common Exercises and Solutions

### Exercise 1: FizzBuzz

```python
def fizzbuzz(n):
    """Prints numbers 1 to n, replacing multiples of 3 with Fizz, 
    multiples of 5 with Buzz, and multiples of both with FizzBuzz"""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
```

### Exercise 2: Factorial Function

```python
def factorial(n):
    """Calculates the factorial of n"""
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Recursive version
def factorial_recursive(n):
    """Calculates factorial recursively"""
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
```

### Exercise 3: Prime Number Checker

```python
def is_prime(n):
    """Checks if a number is prime"""
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    """Prints all prime numbers up to limit"""
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")
    print()
```

## 7. Debugging Tips

### Common Mistakes to Avoid

1. **Indentation Errors**: Python uses indentation to define code blocks
2. **Infinite Loops**: Always ensure loop conditions will eventually become False
3. **Variable Scope Issues**: Be careful with global vs local variables
4. **Off-by-One Errors**: Remember that range(n) goes from 0 to n-1
5. **Function Return Values**: Don't forget to return values when needed

### Debugging Techniques

```python
# Use print statements for debugging
def debug_function(x):
    print(f"Input: {x}")  # Debug print
    result = x * 2
    print(f"Result: {result}")  # Debug print
    return result

# Use assert statements for testing
def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b
```

## 8. Practice Projects

### Project 1: Number Guessing Game

```python
import random

def guessing_game():
    """A simple number guessing game"""
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("I'm thinking of a number between 1 and 100!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
            attempts += 1
            
            if guess == number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Sorry! The number was {number}. Better luck next time!")
```

### Project 2: Simple Calculator

```python
def calculator():
    """A simple calculator program"""
    
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        if y == 0:
            return "Error: Division by zero!"
        return x / y
    
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                
                print(f"Result: {result}")
                
            except ValueError:
                print("Error: Please enter valid numbers!")
        else:
            print("Invalid choice!")
```

## Summary

This module covers the fundamental control structures and function concepts in Python. Master these concepts through practice and experimentation. Remember that good programming involves not just writing code that works, but code that is readable, maintainable, and follows best practices.

Key takeaways:
- Use conditional statements to make decisions in your code
- Employ loops for repetitive tasks and iteration
- Create functions to organize code and promote reusability
- Understand variable scope to avoid common pitfalls
- Practice with real projects to solidify your understanding
