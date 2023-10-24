#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const requesturl = process.argv[2];
const filepath = process.argv[3];

request(requesturl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(filepath, body, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
