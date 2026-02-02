#!/usr/bin/env node
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

function callback (err) {
    if (err) {
        console.log(err);
        return null;
    }
}

fs.writeFile(filePath, content, "utf-8", callback);
