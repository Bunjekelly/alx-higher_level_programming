#!/usr/bin/node

const string = 'C is fun';
const count = Number(process.argv[2]);
if (count) {
  for (let i = 0; i < count; i++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
