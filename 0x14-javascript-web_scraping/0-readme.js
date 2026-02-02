#!/usr/bin/env node
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    console.log(data);
});
