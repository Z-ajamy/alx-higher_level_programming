# 0x12 JavaScript Warm Up

## Overview

This project serves as an introductory guide to JavaScript programming fundamentals. It covers basic concepts such as variables, data types, functions, control flow, and command-line argument handling using Node.js. This warm-up project prepares you for more advanced JavaScript and web development work.

## Learning Objectives

By the end of this project, you should be able to:

- Understand JavaScript syntax and basic concepts
- Work with variables and different data types
- Use operators and control flow statements
- Write and call functions
- Handle command-line arguments with Node.js
- Understand variable scope and hoisting
- Work with strings and string manipulation
- Implement loops and iterations
- Use conditional statements effectively
- Understand the differences between JavaScript and Python

## Requirements

### General Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 18.04 LTS using Node.js (version 10.x)
- All files should end with a newline
- All files must be executable
- The first line of all files should be exactly `#!/usr/bin/node`
- A comment explaining the purpose of the script is recommended
- No use of `var` - use `const` or `let` instead
- Code should be well-formatted and readable

### Installation

```bash
# Install Node.js 10.x
sudo apt-get update
sudo apt-get install -y nodejs npm

# Verify installation
node --version
npm --version
```

## Project Structure

```
0x12-javascript-warm_up/
├── 0-javascript_is_amazing.js
├── 1-multi_languages.js
├── 2-arguments.js
├── 3-value_argument.js
├── 4-concat.js
├── 5-to_integer.js
├── 6-multi_languages_loop.js
├── 7-multi_c.js
├── 8-square.js
├── 9-add.js
├── 10-factorial.js
└── README.md
```

## JavaScript vs Python Quick Reference

| Concept | Python | JavaScript |
|---------|--------|-----------|
| Print | `print()` | `console.log()` |
| Comments | `# comment` | `// comment` |
| Variables | `x = 5` | `const x = 5;` |
| Strings | `"string"` | `"string"` or `'string'` |
| Arrays | `[1, 2, 3]` | `[1, 2, 3]` |
| Objects | `{"key": value}` | `{key: value}` |
| Functions | `def func():` | `function func() {}` |
| Arrow Functions | N/A | `const func = () => {}` |
| If Statement | `if x > 5:` | `if (x > 5) {}` |
| For Loop | `for i in range(10):` | `for (let i = 0; i < 10; i++)` |

## Detailed Task Examples

### Task 0: JavaScript is Amazing (0-javascript_is_amazing.js)
Write a script that prints a string to the console.

**Concepts:** Basic console output, string literals

```javascript
#!/usr/bin/node
console.log('JavaScript is amazing');
```

**Key Points:**
- `console.log()` is used to print output
- Semicolons are optional but recommended
- Use single or double quotes for strings

### Task 1: Multi Languages (1-multi_languages.js)
Write a script that prints strings in multiple languages.

**Concepts:** Multiple console.log statements

```javascript
#!/usr/bin/node
console.log('C is fun');
console.log('Python is cool');
console.log('JavaScript is amazing');
```

**Key Points:**
- Each `console.log()` prints on a new line
- Strings are displayed exactly as written

### Task 2: Arguments (2-arguments.js)
Write a script that prints the number of command-line arguments passed.

**Concepts:** Accessing command-line arguments, `process.argv`

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);
console.log(args.length);
```

**Key Points:**
- `process.argv` contains all command-line arguments
- `process.argv[0]` is the Node.js executable
- `process.argv[1]` is the script path
- `slice(2)` gets arguments starting from index 2
- Usage: `./2-arguments.js arg1 arg2 arg3`

### Task 3: Value Argument (3-value_argument.js)
Write a script that prints the first argument passed to it.

**Concepts:** Accessing specific command-line arguments

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
    console.log('No argument');
} else {
    console.log(args[0]);
}
```

**Key Points:**
- Check if arguments exist before accessing them
- Use array indexing to get specific arguments
- Conditional statements for validation

### Task 4: Concat (4-concat.js)
Write a script that concatenates multiple arguments.

**Concepts:** String concatenation, working with arrays

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);
let result = '';
for (let i = 0; i < args.length; i++) {
    result += args[i];
}
console.log(result);
```

**Alternative using join():**
```javascript
#!/usr/bin/node
const args = process.argv.slice(2);
console.log(args.join(''));
```

**Key Points:**
- String concatenation with `+` operator
- Array `.join()` method combines array elements
- Loops iterate through arrays

### Task 5: To Integer (5-to_integer.js)
Write a script that converts an argument to an integer and performs operations.

**Concepts:** Type conversion, parsing strings to numbers

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Not a number');
} else {
    const num = parseInt(args[0], 10);
    if (isNaN(num)) {
        console.log('Not a number');
    } else if (num === 89) {
        console.log('89 is a perfect number');
    } else {
        console.log(`${num} is ${num > 89 ? 'greater' : 'less'} than 89`);
    }
}
```

**Key Points:**
- `parseInt()` converts string to integer
- `isNaN()` checks if value is not a number
- Template literals use backticks for string interpolation
- Ternary operator for conditional expressions

### Task 6: Multi Languages Loop (6-multi_languages_loop.js)
Write a script that prints strings using a loop.

**Concepts:** Loops, arrays, iteration

```javascript
#!/usr/bin/node
const languages = [
    'C is fun',
    'Python is cool',
    'JavaScript is amazing'
];

for (let i = 0; i < languages.length; i++) {
    console.log(languages[i]);
}
```

**Alternative using forEach():**
```javascript
#!/usr/bin/node
const languages = [
    'C is fun',
    'Python is cool',
    'JavaScript is amazing'
];

languages.forEach(lang => console.log(lang));
```

**Key Points:**
- Traditional `for` loop syntax
- `.length` property for array size
- `forEach()` method for iteration
- Arrow functions with `=>` syntax

### Task 7: Multi C (7-multi_c.js)
Write a script that prints a specific string multiple times based on an argument.

**Concepts:** String repetition, loops with variables

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Missing number argument');
} else {
    const num = parseInt(args[0], 10);
    if (isNaN(num)) {
        console.log('Missing number argument');
    } else {
        for (let i = 0; i < num; i++) {
            console.log('C');
        }
    }
}
```

**Alternative using repeat():**
```javascript
#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Missing number argument');
} else {
    const num = parseInt(args[0], 10);
    if (isNaN(num)) {
        console.log('Missing number argument');
    } else {
        console.log('C\n'.repeat(num).trim());
    }
}
```

**Key Points:**
- `.repeat()` method repeats a string
- Loop control for repetitive tasks
- Input validation

### Task 8: Square (8-square.js)
Write a script that prints a square using a specific character.

**Concepts:** Nested loops, string building

```javascript
#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Missing size argument');
} else {
    const size = parseInt(args[0], 10);
    if (isNaN(size)) {
        console.log('Missing size argument');
    } else {
        for (let i = 0; i < size; i++) {
            console.log('X'.repeat(size));
        }
    }
}
```

**Key Points:**
- Nested loops for 2D patterns
- `.repeat()` for horizontal repetition
- Pattern generation

### Task 9: Add (9-add.js)
Write a script that adds two integers.

**Concepts:** Function definition, return values

```javascript
#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const args = process.argv.slice(2);

if (args.length < 2) {
    console.log('Usage: ./9-add.js <num1> <num2>');
} else {
    const num1 = parseInt(args[0], 10);
    const num2 = parseInt(args[1], 10);
    
    if (isNaN(num1) || isNaN(num2)) {
        console.log('Usage: ./9-add.js <num1> <num2>');
    } else {
        console.log(add(num1, num2));
    }
}
```

**Key Points:**
- Function declaration with `function` keyword
- Return statements
- Multiple parameter validation
- Function calls with arguments

### Task 10: Factorial (10-factorial.js)
Write a script that calculates the factorial of a number.

**Concepts:** Recursion, mathematical operations

```javascript
#!/usr/bin/node

function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Usage: ./10-factorial.js <number>');
} else {
    const num = parseInt(args[0], 10);
    
    if (isNaN(num) || num < 0) {
        console.log('Usage: ./10-factorial.js <number>');
    } else {
        console.log(factorial(num));
    }
}
```

**Alternative using iteration:**
```javascript
#!/usr/bin/node

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Usage: ./10-factorial.js <number>');
} else {
    const num = parseInt(args[0], 10);
    
    if (isNaN(num) || num < 0) {
        console.log('Usage: ./10-factorial.js <number>');
    } else {
        console.log(factorial(num));
    }
}
```

**Key Points:**
- Recursive function calls
- Base cases for recursion
- Mathematical operations (`*=`)
- Loop-based alternatives to recursion

## JavaScript Fundamentals

### Variables and Data Types

```javascript
// Let (block-scoped, can be reassigned)
let name = 'John';
name = 'Jane';  // OK

// Const (block-scoped, cannot be reassigned)
const age = 25;
// age = 26;  // Error

// Data types
const str = 'string';
const num = 42;
const bool = true;
const obj = { key: 'value' };
const arr = [1, 2, 3];
const undef = undefined;
const nul = null;
```

### Operators

```javascript
// Arithmetic
const sum = 10 + 5;      // 15
const diff = 10 - 5;     // 5
const product = 10 * 5;  // 50
const quotient = 10 / 5; // 2
const remainder = 10 % 3; // 1

// Comparison
10 > 5    // true
10 < 5    // false
10 === 10 // true (strict equality)
10 == '10' // true (loose equality)
10 !== 5  // true

// Logical
true && false  // false
true || false  // true
!true          // false
```

### Strings

```javascript
// String literals
const str1 = 'single quotes';
const str2 = "double quotes";
const str3 = `template ${variable}`;  // interpolation

// String methods
const str = 'hello world';
str.length;           // 11
str.toUpperCase();    // 'HELLO WORLD'
str.toLowerCase();    // 'hello world'
str.charAt(0);        // 'h'
str.slice(0, 5);      // 'hello'
str.split(' ');       // ['hello', 'world']
str.includes('world'); // true
str.replace('world', 'JavaScript'); // 'hello JavaScript'
```

### Arrays

```javascript
// Array creation
const arr = [1, 2, 3, 4, 5];
const empty = [];
const mixed = [1, 'two', { three: 3 }];

// Array methods
arr.length;           // 5
arr[0];              // 1
arr.push(6);         // adds to end
arr.pop();           // removes from end
arr.shift();         // removes from beginning
arr.unshift(0);      // adds to beginning
arr.slice(1, 3);     // [2, 3]
arr.indexOf(3);      // 2
arr.includes(3);     // true
arr.join(',');       // '1,2,3,4,5'
arr.map(x => x * 2); // [2, 4, 6, 8, 10]
arr.filter(x => x > 2); // [3, 4, 5]
arr.forEach(x => console.log(x));
```

### Objects

```javascript
// Object creation
const obj = {
    name: 'John',
    age: 25,
    email: 'john@example.com'
};

// Access properties
obj.name;        // 'John'
obj['age'];      // 25

// Modify properties
obj.name = 'Jane';
obj['age'] = 26;
obj.city = 'NYC';  // add new property

// Object methods
Object.keys(obj);      // ['name', 'age', 'email', 'city']
Object.values(obj);    // ['Jane', 26, 'john@example.com', 'NYC']
Object.entries(obj);   // [['name', 'Jane'], ...]
```

### Control Flow

```javascript
// If-else
if (age > 18) {
    console.log('Adult');
} else if (age > 13) {
    console.log('Teenager');
} else {
    console.log('Child');
}

// Switch
switch (day) {
    case 'Monday':
        console.log('Start of week');
        break;
    case 'Friday':
        console.log('End of week');
        break;
    default:
        console.log('Midweek');
}

// Ternary
const status = age > 18 ? 'Adult' : 'Minor';
```

### Loops

```javascript
// For loop
for (let i = 0; i < 5; i++) {
    console.log(i);  // 0, 1, 2, 3, 4
}

// While loop
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// Do-while
let j = 0;
do {
    console.log(j);
    j++;
} while (j < 5);

// For-of (iterate values)
const arr = ['a', 'b', 'c'];
for (const item of arr) {
    console.log(item);  // 'a', 'b', 'c'
}

// For-in (iterate keys)
const obj = { x: 1, y: 2 };
for (const key in obj) {
    console.log(key);  // 'x', 'y'
}
```

### Functions

```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Function expression
const add = function(a, b) {
    return a + b;
};

// Arrow function
const multiply = (a, b) => a * b;

// Arrow function with block
const divide = (a, b) => {
    if (b === 0) {
        return 'Cannot divide by zero';
    }
    return a / b;
};

// Function calls
greet('John');      // 'Hello, John!'
add(5, 3);         // 8
multiply(5, 3);    // 15
divide(10, 2);     // 5
```

## Running Scripts

### Making Scripts Executable

```bash
chmod +x script.js
```

### Running Scripts

```bash
# With proper shebang
./0-javascript_is_amazing.js

# Using Node.js directly
node 0-javascript_is_amazing.js
```

### Passing Arguments

```bash
./2-arguments.js arg1 arg2 arg3
./5-to_integer.js 42
./8-square.js 5
```

## Best Practices

1. **Use `const` by default, `let` when needed**
   ```javascript
   const x = 5;  // Good - unlikely to change
   let counter = 0;  // OK - will change
   ```

2. **Use template literals for string interpolation**
   ```javascript
   // Good
   console.log(`The answer is ${answer}`);
   
   // Avoid
   console.log('The answer is ' + answer);
   ```

3. **Validate input arguments**
   ```javascript
   if (args.length === 0) {
       console.log('Error message');
       return;
   }
   ```

4. **Use meaningful variable names**
   ```javascript
   // Good
   const numberOfStudents = 25;
   
   // Bad
   const n = 25;
   ```

5. **Write functions for reusable code**
   ```javascript
   function calculateSum(a, b) {
       return a + b;
   }
   ```

6. **Handle edge cases**
   ```javascript
   if (isNaN(num)) {
       console.log('Invalid input');
   }
   ```

## Common Pitfalls

### Pitfall 1: Loose vs Strict Equality
```javascript
// Problem
if (x == 5)  // 5 == '5' is true!

// Solution
if (x === 5) // 5 === '5' is false
```

### Pitfall 2: Forgetting parseInt Radix
```javascript
// Problem
parseInt('09');  // Returns 9 (sometimes treated as octal)

// Solution
parseInt('09', 10); // Explicitly specify base 10
```

### Pitfall 3: Not Checking Array Length
```javascript
// Problem
const first = args[0];  // Error if args is empty

// Solution
if (args.length > 0) {
    const first = args[0];
}
```

### Pitfall 4: Using var
```javascript
// Avoid
var x = 5;  // Function-scoped, hoisted issues

// Use
const x = 5;  // Block-scoped, clear intent
```

## Debugging

### Console Methods

```javascript
// Logging
console.log('message');
console.error('error message');
console.warn('warning message');
console.table(array);
console.group('Group');
console.groupEnd();

// Timing
console.time('timer');
// code here
console.timeEnd('timer');
```

## Testing

```bash
# Run a single script
node 0-javascript_is_amazing.js

# Run with arguments
node 5-to_integer.js 42
node 8-square.js 3
```

## Resources

- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Node.js Documentation](https://nodejs.org/en/docs/)
- [JavaScript.info Tutorial](https://javascript.info/)
- [Eloquent JavaScript](https://eloquentjavascript.net/)
- [JavaScript Best Practices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)

## Common JavaScript Gotchas

### Type Coercion
```javascript
'5' + 3      // '53' (string concatenation)
'5' - 3      // 2 (numeric subtraction)
'5' == 5     // true (loose equality)
'5' === 5    // false (strict equality)
```

### Undefined vs Null
```javascript
let x;
console.log(x);  // undefined (declared but not assigned)

const y = null;  // null (intentionally empty)
```

### Hoisting
```javascript
console.log(x);  // undefined (hoisted but not initialized)
var x = 5;

func();  // Works (function hoisted)
function func() {}

arrow();  // Error (arrow functions not hoisted)
const arrow = () => {};
```

## License

This project is part of the ALX Software Engineering Program.
