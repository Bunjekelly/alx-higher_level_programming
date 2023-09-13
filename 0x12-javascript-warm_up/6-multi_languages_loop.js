#!/usr/bin/node

const strings = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let output = '';
for (let i = 0; i < 3; i++) {
  output += strings[i] + '\n';
}

console.log(output);
