#!/usr/bin/node

/**
 * Module: movie_title_fetcher
 *
 * This module fetches and prints the title of a movie from the Star Wars API
 * based on a movie ID provided as a command-line argument. It uses the `request`
 * module to make an HTTP request to the Star Wars API.
 *
 * Usage:
 *   node movie_title_fetcher.js <movie_id>
 *
 * Where `<movie_id>` is the ID of the movie whose title you want to fetch.
 */

const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from command-line arguments

/**
 * Fetches and prints the title of a movie by its ID.
 *
 * This function constructs the URL using the provided movie ID and makes an
 * HTTP request to the Star Wars API. If an error occurs during the request, 
 * it logs the error to the console. Otherwise, it parses the JSON response 
 * and prints the movie title.
 *
 * Args:
 *   id (string): The ID of the movie whose title is to be fetched.
 *
 * Returns:
 *   void
 */
const getMovieTitle = (id) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}/`; // Construct the URL with the movie ID
  
  request(url, (error, response, body) => {
    if (error) {
      console.error(error); // Print the error object if an error occurs
    } else {
      const data = JSON.parse(body); // Parse the JSON response
      console.log(data.title); // Print the movie title
    }
  });
};

// Ensure the movie ID argument is provided
if (movieId) {
  getMovieTitle(movieId);
} else {
  console.error('No movie ID provided');
}
