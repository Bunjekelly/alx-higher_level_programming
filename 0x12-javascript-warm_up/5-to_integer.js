#!/usr/bin/node

const args = process.argv[2];
const conargs = Number(args);

if ((conargs === undefined) || isNaN(conargs)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${conargs}`);
}
