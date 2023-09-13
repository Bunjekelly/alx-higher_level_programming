#!/usr/bin/node

const args = process.argv.slice(2);

if (!args[0] || !args[1]) {
  console.log('Two arguments are required');
} else {
  console.log(`${args[0]} is ${args[1]}`);
}
