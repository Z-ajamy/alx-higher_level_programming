#!/usr/bin/env node
const request = require('request');

const options = {
    url : process.argv[2],
    method : "GET"
};

function callback (err, response, body) {
    if (err) {
        console.log(err);
        return null;
    }
    console.log("code: " + response.statusCode);
}

request(options, callback);
