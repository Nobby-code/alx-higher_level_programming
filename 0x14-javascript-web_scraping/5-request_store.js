#!/usr/bin/node

/* script to get the content of a web page and stores it in a file */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log('code:', res.statusCode);
  } else {
    fs.writeFile(fileName, res.body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
