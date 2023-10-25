#!/usr/bin/node

const request = require('request');

const apiurl = process.argv[2];

request(apiurl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;

    const Movies = data.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));

    console.log(`${Movies.length}`);
  }
});
