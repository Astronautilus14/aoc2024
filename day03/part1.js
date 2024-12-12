// const fs = require("fs");

// const r = /mul\(\d{1,3},\d{1,3}\)/g;
// const input = fs.readFileSync('inp.txt', 'utf-8');
// const matches = input.match(r);
// let sum = 0
// for (const match of matches) {
//   sum += match.slice(4,match.length-1).split(',').reduce((acc, cur) => acc *= Number(cur), 1);
// }
// console.log(sum)

console.log(require('fs').readFileSync('inp.txt','utf-8').match(/mul\(\d{1,3},\d{1,3}\)/g).reduce((a,c)=>a+=c.slice(4,c.length-1).split(',').reduce((a,c)=>a*=c,1),0));