#!/usr/bin/node

const request = require('request');

const geturl = process.argv[2];

request(geturl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
