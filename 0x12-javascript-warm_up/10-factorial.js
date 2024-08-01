#!/usr/bin/node

// Define the recursive factorial function
function factorial(n) {
    if (n < 0) {
      return NaN; // Factorial is not defined for negative numbers
    }
    if (n === 0 || n === 1) {
      return 1; // Base case: 0! and 1! are both 1
    }
    return n * factorial(n - 1); // Recursive case
  }
  
  // Get the argument and cast it to an integer
  const input = parseInt(process.argv[2], 10);
  
  // Compute the factorial and print the result
  console.log(factorial(isNaN(input) ? NaN : input));
  