const input = require('fs').readFileSync('inp.txt', 'utf-8');

let c = 0
for (const l of input.split('\n')) {
  let [target, nums] = l.split(': ')
  target = Number(target)
  nums = nums.split(' ').map(Number)

  for (let i = 0; i < 3 ** (nums.length - 1); i++) {
    res = nums[0]
    const operators = i.toString(3).padStart(nums.length - 1, 0)

    for (let j = 1; j < nums.length; j++) {
      const operator = operators[j-1]
      if (operator === '0') {
        res += nums[j]
      } else if (operator === '1') {
        res *= nums[j]
      } else {
        res = Number(res.toString() + nums[j].toString())
      }
    }

    if (res == target) {
      c += res;
      break;
    }
  }
}
console.log(c)