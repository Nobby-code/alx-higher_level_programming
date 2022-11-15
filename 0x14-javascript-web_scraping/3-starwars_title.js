#!/usr/bin/node

/* script that prints the title of a war star movie
   where episode number matches a given integer
*/

const request = require('request');
const movieId = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
