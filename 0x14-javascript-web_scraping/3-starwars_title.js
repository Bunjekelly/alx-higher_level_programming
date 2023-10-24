#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const geturl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(geturl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);

    console.log(data.title);
  }
});
