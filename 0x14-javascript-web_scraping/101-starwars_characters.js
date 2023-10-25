#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiurl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiurl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body).characters;
  PrintCharacters(data, 0);
});

function PrintCharacters (characters, index) {
  if (index < characters.length) {
    request(characters[index], (err, response, body) => {
      if (err) {
        console.error(err);
      }
      const character = JSON.parse(body).name;
      console.log(character);
      PrintCharacters(characters, index + 1);
    });
  }
}
