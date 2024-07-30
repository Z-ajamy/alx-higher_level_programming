#!/usr/bin/node

/**
 * Module: file_writer
 *
 * This module writes a string to a file specified by the file path provided
 * as a command-line argument. It uses the Node.js `fs` module to write data
 * to the file asynchronously.
 *
 * Usage:
 *   node file_writer.js <file_path> <content>
 *
 * Where `<file_path>` is the path to the file you want to write to, and
 * `<content>` is the string you want to write into the file.
 */

const fs = require('fs');
const filePath = process.argv[2]; // Get the file path from command-line arguments
const content = process.argv[3]; // Get the string to write from command-line arguments

/**
 * Writes a string to a file.
 *
 * This function uses Node.js's `fs.writeFile` method to write the data to the
 * specified file asynchronously. If an error occurs during the write operation,
 * the error is logged to the console.
 *
 * Args:
 *   path (string): The path to the file where data should be written.
 *   data (string): The string content to be written to the file.
 *
 * Returns:
 *   void
 */
const writeFile = (path, data) => {
  fs.writeFile(path, data, 'utf8', (err) => {
    if (err) {
      console.error(err); // Print the error object if an error occurs
    }
  });
};

// Ensure both arguments are provided
if (filePath && content) {
  writeFile(filePath, content);
} else {
  console.error('Missing file path or content');
}
