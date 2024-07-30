#!/usr/bin/node

/**
 * Module: status_code_checker
 *
 * This module makes an HTTP request to a specified URL and prints the HTTP status code
 * of the response. It uses the `request` module to perform the HTTP request.
 *
 * Usage:
 *   node status_code_checker.js <url>
 *
 * Where `<url>` is the URL to which the HTTP request is made.
 */

const request = require('request');
const url = process.argv[2]; // Get the URL from command-line arguments

/**
 * Makes an HTTP request to the specified URL and prints the HTTP status code.
 *
 * This function uses the `request` module to perform the HTTP request. If an error
 * occurs during the request, it logs the error to the console. Otherwise, it prints
 * the status code of the HTTP response.
 *
 * Args:
 *   url (string): The URL to make the HTTP request to.
 *
 * Returns:
 *   void
 */
const getStatusCode = (url) => {
  request(url, (error, response) => {
    if (error) {
      console.error(error); // Print the error object if an error occurs
    } else {
      console.log(`code: ${response.statusCode}`); // Print the status code
    }
  });
};

// Ensure the URL argument is provided
if (url) {
  getStatusCode(url);
} else {
  console.error('No URL provided');
}
