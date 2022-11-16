#!/usr/bin/node

/* script to print characters of a Star War movie */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, (err, res, body) => {
  if (err) {
    console.log('code:', res.statusCode);
  } else {
    const result = JSON.parse(res.body);
    for (const character of result.characters) {
      request(character, (err, res, body) => {
        if (err) {
          console.log('code:', res.statusCode);
        }
        console.log(JSON.parse(res.body).name);
      });
    }
  }
});
