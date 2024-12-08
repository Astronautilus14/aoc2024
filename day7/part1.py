f = open('inp.txt', 'r')

c = 0
for l in f.readlines():
  target, nums = l.split(': ')
  target = int(target)
  nums = [int(n) for n in nums.strip().split(' ')]
  for i in range(2**(len(nums)-1)):
    res = nums[0]
    for j, num in enumerate(nums[1:]):
      # Get bit at position j in i
      add = i & (2**j) > 0
      if add:
        res += num
      else:
        res *= num
    if res == target:
      c += res
      break

print(c)