#!/usr/bin/node

/*
 printing the number of movies by filtering a character
*/

const request = require('request');
const url = process.argv[2];

let count = 0;

request(url, (err, res, body) => {
  if (err) {
    console.log('code:', res.statusCode);
  } else {
    const result = JSON.parse(body);

    for (const film of result.results) {
      for (const value of film.characters) {
        if (value.includes('18')) count++;
      }
    }
    console.log(count);
  }
});
