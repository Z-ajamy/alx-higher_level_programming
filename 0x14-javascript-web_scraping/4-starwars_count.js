#!/usr/bin/node

/**
 * Module: wedge_antilles_movie_counter
 *
 * This module counts and prints the number of movies featuring Wedge Antilles from
 * the Star Wars API. The API URL is provided as a command-line argument. It uses
 * the `request` module to make HTTP requests to the API.
 *
 * Usage:
 *   node wedge_antilles_movie_counter.js <api_url>
 *
 * Where `<api_url>` is the URL endpoint to fetch the list of films.
 */

const request = require('request');
const apiUrl = process.argv[2]; // Get the API URL from command-line arguments
const wedgeAntillesId = 18; // Wedge Antilles character ID

/**
 * Counts and prints the number of movies featuring Wedge Antilles.
 *
 * This function makes an HTTP request to the specified API URL. It parses the JSON
 * response to extract the list of films and checks each film to see if Wedge Antilles
 * (identified by his character ID) is listed in the film's character list. It then
 * prints the count of such films.
 *
 * Args:
 *   url (string): The API URL to fetch the list of films.
 *
 * Returns:
 *   void
 */
const countMoviesWithCharacter = (url) => {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error); // Print the error object if an error occurs
    } else {
      const data = JSON.parse(body); // Parse the JSON response
      const films = data.results; // Get the list of films
      let count = 0; // Initialize the count of movies

      // Loop through each film to check if Wedge Antilles is in the characters list
      films.forEach((film) => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
          count++;
        }
      });

      console.log(count); // Print the count of movies featuring Wedge Antilles
    }
  });
};

// Ensure the API URL argument is provided
if (apiUrl) {
  countMoviesWithCharacter(apiUrl);
} else {
  console.error('No API URL provided');
}
