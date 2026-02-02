#!/usr/bin/env node

const request = require('request');

const url = process.argv[2];

request(url, { json: true }, function (err, response, body) {
    if (err) {
        console.log(err);
        return;
    }

    const completedTasks = {};

    for (let i = 0; i < body.length; i++) {
        const task = body[i];

        if (task.completed === true) {
            
            if (!completedTasks[task.userId]) {
                completedTasks[task.userId] = 1;
            } else {
                completedTasks[task.userId] += 1;
            }
        }
    }

    console.log(completedTasks);
});
