#!/usr/bin/env node

const request = require('request');


const options = {
    url: process.argv[2],
    json: true
}

function callback (err, response, body) {
    if (err) {
        console.log(err);
        return null;
    }
    console.log(body['title']);
};

request(options, callback);
