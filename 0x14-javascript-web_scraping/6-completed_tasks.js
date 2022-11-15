#!/usr/bin/node

/* script to compute the number of tasks completed by user Id */

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log('code:', err);
  } else {
    const resBody = JSON.parse(res.body);
    const tasksCompleted = {};

    for (const todo of resBody) {
      if (todo.completed) {
        if (tasksCompleted[todo.userId]) {
          tasksCompleted[todo.userId] += 1;
        } else {
          tasksCompleted[todo.userId] = 1;
        }
      }
    }
    console.log(tasksCompleted);
  }
});
