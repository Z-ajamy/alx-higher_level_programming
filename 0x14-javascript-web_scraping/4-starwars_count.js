#!/usr/bin/env node

/**
 * @fileoverview Star Wars API character counter.
 * 
 * This script fetches movie data from the Star Wars API and counts how many
 * films feature a specific character (Luke Skywalker, identified by ID 18)
 * in their character roster.
 * 
 * Usage:
 *   node script.js <swapi-url>
 * 
 * Example:
 *   node script.js "https://swapi.dev/api/films/"
 * 
 * @requires request
 */

const request = require('request');

/**
 * Configuration object for the HTTP request to the Star Wars API.
 * 
 * @type {Object}
 * @property {string} url - The API endpoint URL from command line arguments.
 * @property {boolean} json - Flag to automatically parse JSON response body.
 */
const options = {
    url: process.argv[2],
    json: true
}

/**
 * Processes the API response and counts films featuring a specific character.
 * 
 * This callback handles the HTTP response from the Star Wars API. It extracts
 * the results array, iterates through each film's character list, and counts
 * occurrences where the character ID matches the target (character ID 18).
 * 
 * The character identification is based on the character URL pattern, where
 * URLs ending with '/18/' represent a specific character across all films.
 * 
 * @param {Error|null} err - Error object if the request failed, null otherwise.
 * @param {Object} response - The HTTP response object from the request library.
 * @param {Object} body - The parsed JSON response body containing film data.
 * @param {Array<Object>} body.results - Array of film objects from the API.
 * @param {Array<string>} body.results[].characters - Array of character URLs
 *     for each film.
 * 
 * @returns {null} Returns null if an error occurs during processing.
 * 
 * @example
 *   request(options, callback);
 *   Output: Prints the count of films matching the criteria to console.
 */
function callback (err, response, body) {
    if (err) {
        console.log(err);
        return null;
    }
    
    const movies = body.results;
    let num = 0;

    for (let index = 0; index < movies.length; index++) {
        for (let j = 0; j < movies[index].characters.length; j++){
            if (movies[index].characters[j].endsWith('/18/')) {
                num += 1;
                j++;
                break;
            }
        }
    }
    
    console.log(num);
};

request(options, callback);
