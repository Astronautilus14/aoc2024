const fs = require("fs");

const input = fs.readFileSync('inp.txt', 'utf-8');
const r = /mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)/g
const matches = input.match(r);

let sum = 0
let enabled = true
for (const match of matches) {
  if (match == 'do()') {
    enabled = true
  } else if (match == "don't()") {
    enabled = false
  } else if (enabled) {
    sum += match.slice(4,match.length-1).split(',').reduce((acc, cur) => acc *= Number(cur), 1);
  }
}
console.log(sum)