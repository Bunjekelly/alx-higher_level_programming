#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiurl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiurl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);

  data.characters.forEach(characterurl => {
    request(characterurl, (err, response, body) => {
      if (err) {
        console.error(err);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
