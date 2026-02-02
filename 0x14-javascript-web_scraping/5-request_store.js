#!/usr/bin/env node

/**
 * @fileoverview HTTP response downloader with file persistence.
 * 
 * This script fetches content from an HTTP API endpoint and persists the
 * response body to a local file. It handles errors at each stage of the
 * request-response-write pipeline and provides console feedback on failures.
 * 
 * Usage:
 *   node script.js <api-url> <output-filepath>
 * 
 * Example:
 *   node script.js "https://api.example.com/data" "./output.json"
 * 
 * @requires fs - File system module for writing downloaded content to disk.
 * @requires request - HTTP request library for fetching API data.
 */

const fs = require('fs');
const request = require('request');

/**
 * API endpoint URL provided via command line argument.
 * 
 * @type {string}
 */
let api = process.argv[2];

/**
 * Destination file path for the downloaded content.
 * 
 * @type {string}
 */
let fpath = process.argv[3];

/**
 * Configuration object for the HTTP request to the API endpoint.
 * 
 * @type {Object}
 * @property {string} url - The API endpoint URL to fetch data from.
 */
const options = {
    'url': api,
};

/**
 * Handles the HTTP response from the API request.
 * 
 * This callback receives the response from the API endpoint. If no errors
 * occurred during the request, it extracts the response body and initiates
 * a file write operation to persist the content. The response body is written
 * as UTF-8 encoded text to the specified file path.
 * 
 * @param {Error|null} err - Error object if the HTTP request failed, null
 *     if successful.
 * @param {Object} response - The HTTP response object containing metadata
 *     about the server response.
 * @param {string} body - The raw response body content from the API endpoint.
 * 
 * @returns {null} Returns null if an error occurs during request processing
 *     or if the response body is empty.
 * 
 * @see {@link callbackFile} for file write error handling.
 * 
 * @example
 *   request(options, callbackReq);
 *   Output: Writes response body to file or logs errors to console.
 */
function callbackReq (err, response, body) {
    let content;

    if (err) {
        console.log(err);
        return null;
    }
    content = body;

    if (!content) return null;

    /**
     * Handles errors that occur during the file write operation.
     * 
     * This nested callback is invoked after the fs.writeFile operation
     * completes. If an error occurs while writing to disk, it is logged
     * to the console. Success cases are silent.
     * 
     * @param {Error|null} err - Error object if the file write failed, null
     *     if the write completed successfully.
     * 
     * @returns {null} Returns null if an error occurs during file writing.
     */
    function callbackFile (err) {
        if (err) {
            console.log(err);
            return null;
        }
    }

    fs.writeFile(fpath, content, 'UTF-8', callbackFile);
}

request(options, callbackReq);
