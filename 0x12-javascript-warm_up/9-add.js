#!/usr/bin/node

// Define the add function
function add(a, b) {
    return a + b;
  }
  
  // Extract arguments and convert them to integers
  const num1 = parseInt(process.argv[2], 10);
  const num2 = parseInt(process.argv[3], 10);
  
  // Print the result of adding the two integers
  console.log(add(num1, num2));
  