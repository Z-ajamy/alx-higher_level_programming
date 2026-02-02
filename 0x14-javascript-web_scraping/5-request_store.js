#!/usr/bin/env node
const fs = require('fs');
const request = require('request');

let api = process.argv[2];
let fpath = process.argv[3];


const options = {
    'url': api,
};

function callbackReq (err, response, body) {
    let content;

    if (err) {
        console.log(err);
        return null;
    }
    content = body;

    if (!content) return null;

    function callbackFile (err) {
        if (err) {
            console.log(err);
            return null;
        }
    }
    fs.writeFile(fpath, content,'UTF-8' , callbackFile);

}

request(options, callbackReq);
