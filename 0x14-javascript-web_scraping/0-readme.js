#!/usr/bin/node

/**
 * Module: file_reader
 *
 * This module reads and prints the content of a file specified by the file path
 * provided as a command-line argument. It uses the Node.js `fs` module to read
 * the file asynchronously.
 *
 * Usage:
 *   node file_reader.js <file_path>
 *
 * Where `<file_path>` is the path to the file you want to read.
 */

const fs = require('fs');
const filePath = process.argv[2]; // Get the file path from command-line arguments

/**
 * Reads and prints the content of a file.
 *
 * This function uses Node.js's `fs.readFile` method to read the file asynchronously.
 * If an error occurs while reading the file, the error is logged to the console.
 * Otherwise, the content of the file is printed to the console.
 *
 * Args:
 *   path (string): The path to the file to read.
 *
 * Returns:
 *   void
 */
const readFile = (path) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      console.error(err); // Print the error object if an error occurs
    } else {
      console.log(data); // Print the file content if successful
    }
  });
};

// Ensure the file path argument is provided
if (filePath) {
  readFile(filePath);
} else {
  console.error('No file path provided');
}
