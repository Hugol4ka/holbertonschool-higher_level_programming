#!/usr/bin/node

const argv = process.argv;

if (process.argv.length === 2) {
  console.log('No argument');
}
console.log(argv[2]);
