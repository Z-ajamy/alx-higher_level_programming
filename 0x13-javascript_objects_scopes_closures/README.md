# 0x13 JavaScript Objects, Scopes, and Closures

## Overview

This project dives deeper into JavaScript by exploring objects, scope, and closures. You will learn how to create classes and objects, understand variable scope in JavaScript, implement closures, and build more complex data structures. These concepts are fundamental to object-oriented programming in JavaScript and are essential for writing maintainable, modular code.

## Learning Objectives

By the end of this project, you should be able to:

- Create and manipulate JavaScript objects
- Understand and apply different types of scope (global, function, block)
- Implement closures and understand their use cases
- Work with `this` keyword and context binding
- Create and use classes with inheritance
- Implement getters and setters
- Use prototype-based inheritance
- Handle object property access and modification
- Understand the scope chain
- Apply closures to create private variables and methods

## Requirements

### General Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 18.04 LTS using Node.js (version 10.x)
- All files should end with a newline
- All files must be executable
- The first line of all files should be exactly `#!/usr/bin/node`
- Code should follow good practices without using `var`
- All functions/classes should be documented with JSDoc-style comments
- Code must export functions/classes properly for testing

### Installation

```bash
sudo apt-get update
sudo apt-get install -y nodejs npm
node --version
npm --version
```

## Project Structure

```
0x13-javascript_objects_scopes_closures/
├── 0-rectangle.js
├── 0-main.js
├── 1-rectangle.js
├── 1-main.js
├── 2-rectangle.js
├── 2-main.js
├── 3-rectangle.js
├── 3-main.js
├── 4-rectangle.js
├── 4-main.js
├── 5-square.js
├── 5-main.js
├── 6-square.js
├── 6-main.js
├── 7-occurrences.js
├── 7-main.js
├── 8-esrever.js
├── 8-main.js
├── 9-logme.js
├── 9-main.js
├── 10-converter.js
├── 10-main.js
└── README.md
```

## Core Concepts

### 1. Objects in JavaScript

Objects are collections of key-value pairs. They can store data and methods.

```javascript
// Object literal
const person = {
    name: 'John',
    age: 30,
    greet() {
        console.log(`Hello, I'm ${this.name}`);
    }
};

person.name;      // 'John'
person.greet();   // Hello, I'm John
```

### 2. Scope in JavaScript

Scope determines where variables are accessible.

```javascript
// Global scope
const global = 'global';

function outer() {
    // Function scope
    const functionScoped = 'function';
    
    function inner() {
        // Inner function scope
        const blockScoped = 'block';
        console.log(global, functionScoped, blockScoped); // All accessible
    }
    
    console.log(global, functionScoped); // OK
    // console.log(blockScoped);  // Error - out of scope
}
```

### 3. Closures

A closure is a function that has access to variables from its outer scope even after that function has returned.

```javascript
function makeCounter() {
    let count = 0;  // Private variable
    
    return {
        increment() {
            return ++count;
        },
        decrement() {
            return --count;
        },
        getCount() {
            return count;
        }
    };
}

const counter = makeCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());  // 2
```

### 4. The `this` Keyword

`this` refers to the object on which a method is called.

```javascript
const person = {
    name: 'John',
    greet() {
        console.log(`Hello, I'm ${this.name}`);
    }
};

person.greet();  // 'Hello, I'm John' (this = person)

const greet = person.greet;
greet();  // 'Hello, I'm undefined' (this = global or undefined in strict mode)
```

### 5. Classes (ES6)

Classes provide a cleaner syntax for object-oriented programming.

```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    
    area() {
        return this.width * this.height;
    }
}

const rect = new Rectangle(10, 5);
console.log(rect.area()); // 50
```

## Detailed Task Examples

### Task 0: Simple Rectangle (0-rectangle.js)
Create an empty Rectangle class.

**Concepts:** Class definition, constructor

```javascript
#!/usr/bin/node
/**
 * Rectangle class
 */
class Rectangle {
    /**
     * Constructor for Rectangle
     * @param {number} w - width
     * @param {number} h - height
     */
    constructor(w, h) {
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;
```

**Main file (0-main.js):**
```javascript
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle(10, 7);
console.log(r1.width);   // 10
console.log(r1.height);  // 7
console.log(r1);         // Rectangle { width: 10, height: 7 }
```

### Task 1: Rectangle with Validation (1-rectangle.js)
Add validation to rectangle constructor.

**Concepts:** Conditionals in constructor, validation

```javascript
#!/usr/bin/node
/**
 * Rectangle class with validation
 */
class Rectangle {
    /**
     * Constructor for Rectangle with validation
     * @param {number} w - width
     * @param {number} h - height
     */
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return;  // Return empty object if invalid
        }
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;
```

### Task 2: Rectangle with Methods (2-rectangle.js)
Add instance methods to the Rectangle class.

**Concepts:** Instance methods, `this` keyword

```javascript
#!/usr/bin/node
/**
 * Rectangle class with methods
 */
class Rectangle {
    /**
     * Constructor for Rectangle
     * @param {number} w - width
     * @param {number} h - height
     */
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return;
        }
        this.width = w;
        this.height = h;
    }
    
    /**
     * Calculate area of rectangle
     * @returns {number} area
     */
    area() {
        return this.width * this.height;
    }
    
    /**
     * Calculate perimeter of rectangle
     * @returns {number} perimeter
     */
    perimeter() {
        return 2 * (this.width + this.height);
    }
}

module.exports = Rectangle;
```

**Test (2-main.js):**
```javascript
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1.area());      // 6
console.log(r1.perimeter()); // 10

const r2 = new Rectangle(10, 7);
console.log(r2.area());      // 70
console.log(r2.perimeter()); // 34
```

### Task 3: Rectangle with String Representation (3-rectangle.js)
Add a string representation method.

**Concepts:** String building, loops, instanceof

```javascript
#!/usr/bin/node
/**
 * Rectangle class with print method
 */
class Rectangle {
    /**
     * Constructor for Rectangle
     * @param {number} w - width
     * @param {number} h - height
     */
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return;
        }
        this.width = w;
        this.height = h;
    }
    
    /**
     * Area of rectangle
     * @returns {number} area
     */
    area() {
        return this.width * this.height;
    }
    
    /**
     * Perimeter of rectangle
     * @returns {number} perimeter
     */
    perimeter() {
        return 2 * (this.width + this.height);
    }
    
    /**
     * Print rectangle using character
     * @param {string} c - character to use (default 'X')
     */
    print(c = 'X') {
        if (typeof c !== 'string' || c.length !== 1) {
            return;
        }
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = Rectangle;
```

**Test (3-main.js):**
```javascript
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();        // XX
               // XX
               // XX

r1.print('C');     // CC
               // CC
               // CC

r1.print('c');     // (nothing - custom char handling)
```

### Task 4: Rectangle with toString (4-rectangle.js)
Override toString method.

**Concepts:** Method overriding, string templates

```javascript
#!/usr/bin/node
/**
 * Rectangle class with toString
 */
class Rectangle {
    /**
     * Constructor for Rectangle
     * @param {number} w - width
     * @param {number} h - height
     */
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return;
        }
        this.width = w;
        this.height = h;
    }
    
    /**
     * Area of rectangle
     * @returns {number} area
     */
    area() {
        return this.width * this.height;
    }
    
    /**
     * Perimeter of rectangle
     * @returns {number} perimeter
     */
    perimeter() {
        return 2 * (this.width + this.height);
    }
    
    /**
     * Print rectangle using character
     * @param {string} c - character to use (default 'X')
     */
    print(c = 'X') {
        if (typeof c !== 'string' || c.length !== 1) {
            return;
        }
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
    
    /**
     * String representation of rectangle
     * @returns {string} description
     */
    toString() {
        return `Rectangle ${this.width} x ${this.height}`;
    }
}

module.exports = Rectangle;
```

### Task 5: Square (5-square.js)
Create a Square class that inherits from Rectangle.

**Concepts:** Inheritance, super keyword, method overriding

```javascript
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Square class extending Rectangle
 */
class Square extends Rectangle {
    /**
     * Constructor for Square
     * @param {number} size - side length
     */
    constructor(size) {
        super(size, size);
    }
}

module.exports = Square;
```

**Test (5-main.js):**
```javascript
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
console.log(s1.area());      // 16
console.log(s1.perimeter()); // 16
s1.print('C');

const s2 = new Square(2);
s2.print('o');
```

### Task 6: Square with Custom Print (6-square.js)
Override print method in Square class.

**Concepts:** Method overriding in inheritance

```javascript
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Square class with custom print
 */
class Square extends Rectangle {
    /**
     * Constructor for Square
     * @param {number} size - side length
     */
    constructor(size) {
        super(size, size);
    }
    
    /**
     * Print square with border effect
     * @param {string} c - character to use
     */
    charPrint(c = 'X') {
        if (typeof c !== 'string' || c.length !== 1) {
            return;
        }
        for (let i = 0; i < this.height; i++) {
            if (i === 0 || i === this.height - 1) {
                console.log(c.repeat(this.width));
            } else {
                console.log(c + ' '.repeat(this.width - 2) + c);
            }
        }
    }
}

module.exports = Square;
```

### Task 7: Count Occurrences (7-occurrences.js)
Implement closure to count occurrences in a list.

**Concepts:** Closures, higher-order functions

```javascript
#!/usr/bin/node
/**
 * Count occurrences of an element in a list
 * Returns a function that counts specific elements
 * 
 * @param {Array} list - list to search
 * @returns {Function} function that counts element occurrences
 */
exports.occurrences = function(list) {
    return function(element) {
        let count = 0;
        for (const item of list) {
            if (item === element) {
                count++;
            }
        }
        return count;
    };
};
```

**Test (7-main.js):**
```javascript
#!/usr/bin/node
const { occurrences } = require('./7-occurrences');

const list = [1, 2, 3, 2, 2, 4, 5, 2];
const countTwo = occurrences(list);
console.log(countTwo(2));  // 4
console.log(countTwo(1));  // 1
console.log(countTwo(4));  // 1
```

### Task 8: String Reverser (8-esrever.js)
Create a function that reverses a string using reduce.

**Concepts:** Array methods, reduce, closures

```javascript
#!/usr/bin/node
/**
 * Reverse a string using array reduce
 * 
 * @param {string} str - string to reverse
 * @returns {string} reversed string
 */
exports.esrever = function(str) {
    return str.split('').reduce((rev, char) => char + rev, '');
};
```

**Alternative using simple loop:**
```javascript
exports.esrever = function(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
};
```

**Test (8-main.js):**
```javascript
#!/usr/bin/node
const { esrever } = require('./8-esrever');

console.log(esrever('Hello'));      // olleH
console.log(esrever('JavaScript')); // tpircSavaJ
console.log(esrever('1234'));       // 4321
```

### Task 9: Log Message with Counter (9-logme.js)
Track call count for a function using closure.

**Concepts:** Closures with state, counting

```javascript
#!/usr/bin/node
/**
 * Log a message with call count
 * Closure maintains state of call count
 * 
 * @param {string} msg - message to log
 */
exports.logMe = (function() {
    let count = 0;
    
    return function(msg) {
        count++;
        console.log(`${count}: ${msg}`);
    };
})();
```

**Test (9-main.js):**
```javascript
#!/usr/bin/node
const { logMe } = require('./9-logme');

logMe('Hello');     // 1: Hello
logMe('World');     // 2: World
logMe('from JS');   // 3: from JS
logMe('!!');        // 4: !!
```

### Task 10: Number Converter (10-converter.js)
Convert numbers between bases using closure.

**Concepts:** Higher-order functions, closures, base conversion

```javascript
#!/usr/bin/node
/**
 * Create a converter function for a specific base
 * 
 * @param {number} base - target base (2-36)
 * @returns {Function} function that converts to specified base
 */
exports.converter = function(base) {
    return function(num) {
        return num.toString(base);
    };
};
```

**Test (10-main.js):**
```javascript
#!/usr/bin/node
const { converter } = require('./10-converter');

const convert10to2 = converter(2);
const convert10to16 = converter(16);

console.log(convert10to2(2));    // 10
console.log(convert10to2(10));   // 1010
console.log(convert10to2(1000));  // 1111101000

console.log(convert10to16(9));    // 9
console.log(convert10to16(255));  // ff
console.log(convert10to16(1000));  // 3e8
```

## Advanced Concepts

### Getters and Setters

```javascript
class Rectangle {
    constructor(width, height) {
        this._width = width;
        this._height = height;
    }
    
    get width() {
        return this._width;
    }
    
    set width(value) {
        if (value <= 0) throw new Error('Width must be positive');
        this._width = value;
    }
}

const r = new Rectangle(10, 5);
console.log(r.width);  // 10
r.width = 20;          // Uses setter
```

### Static Methods

```javascript
class Math2 {
    static add(a, b) {
        return a + b;
    }
    
    static multiply(a, b) {
        return a * b;
    }
}

console.log(Math2.add(5, 3));      // 8
console.log(Math2.multiply(5, 3)); // 15
```

### Prototype-Based Inheritance

```javascript
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    console.log(`${this.name} makes a sound`);
};

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

const dog = new Dog('Max', 'Labrador');
dog.speak(); // Max makes a sound
```

## Module Exports and Imports

### CommonJS (Node.js)

```javascript
// Exporting
module.exports = ClassName;
module.exports = { function1, function2 };
exports.myFunction = function() {};

// Importing
const MyClass = require('./myFile');
const { myFunction } = require('./myFile');
```

## Best Practices

1. **Use classes for organization**
   ```javascript
   class Rectangle {
       constructor(w, h) {
           this.width = w;
           this.height = h;
       }
   }
   ```

2. **Validate input in constructors**
   ```javascript
   constructor(w, h) {
       if (w <= 0 || h <= 0) return;
       this.width = w;
       this.height = h;
   }
   ```

3. **Use meaningful method names**
   ```javascript
   // Good
   calculateArea()
   getPerimeter()
   
   // Avoid
   calc()
   getPeri()
   ```

4. **Document with JSDoc**
   ```javascript
   /**
    * Calculate rectangle area
    * @returns {number} area in square units
    */
   area() {
       return this.width * this.height;
   }
   ```

5. **Use const/let, not var**
   ```javascript
   // Good
   const width = 10;
   let count = 0;
   
   // Avoid
   var width = 10;
   ```

6. **Leverage closures for private variables**
   ```javascript
   const counter = (() => {
       let count = 0;  // Private
       return {
           increment: () => ++count,
           getCount: () => count
       };
   })();
   ```

7. **Use inheritance for code reuse**
   ```javascript
   class Square extends Rectangle {
       constructor(size) {
           super(size, size);
       }
   }
   ```

## Common Patterns

### Factory Function
```javascript
function createRectangle(width, height) {
    return {
        width,
        height,
        area() {
            return this.width * this.height;
        }
    };
}
```

### Revealing Module Pattern
```javascript
const calculator = (() => {
    const add = (a, b) => a + b;
    const subtract = (a, b) => a - b;
    
    return {
        add,
        subtract
    };
})();
```

### Observer Pattern
```javascript
function createObservable() {
    const observers = [];
    
    return {
        subscribe(callback) {
            observers.push(callback);
        },
        notify(data) {
            observers.forEach(callback => callback(data));
        }
    };
}
```

## Running and Testing

```bash
# Make files executable
chmod +x *.js

# Run test files
./0-main.js
./5-main.js
./10-main.js

# Run with node directly
node 0-main.js
node 5-main.js
node 10-main.js
```

## Troubleshooting

### Issue: "Cannot read property 'width' of undefined"
- Check if constructor returns early due to validation
- Verify object is properly instantiated with `new` keyword

### Issue: Method not found on instance
- Ensure method is defined on the class
- Check for typos in method names
- Verify class is properly exported with `module.exports`

### Issue: Closure not maintaining state
- Verify closure is created with IIFE or returned function
- Check that variable is declared in outer scope
- Ensure function is being called correctly

### Issue: `this` is undefined
- Remember to use `new` keyword when creating instances
- In callbacks, use arrow functions to maintain context
- Or use `.bind()` to manually set context

## Resources

- [MDN: Objects and Prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [MDN: Scope and Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [MDN: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [JavaScript.info: Objects](https://javascript.info/object)
- [JavaScript.info: Scope, Closures](https://javascript.info/closure)

## Key Takeaways

- **Objects** are fundamental data structures in JavaScript
- **Scope** determines variable accessibility (global, function, block)
- **Closures** allow access to outer scope variables and create private state
- **Classes** provide cleaner syntax for object-oriented programming
- **Inheritance** enables code reuse through class extension
- **Modules** organize code and manage dependencies through exports/imports
- **The `this` keyword** refers to the object context
- **Patterns** like factory functions and revealing module provide powerful abstractions

## License

This project is part of the ALX Software Engineering Program.
