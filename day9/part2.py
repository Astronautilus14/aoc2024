f = open('inp.txt', 'r')
nums = [(i//2 if i%2==0 else -1, int(x)) for i, x in enumerate(f.readline())]

def printNums(n):
  print("".join((f"{x[0]}" if x[0] != -1 else '.') * x[1] for x in n))

#printNums(nums)

for i in range(len(nums)-1,0,-1):
  idx1, size1 = nums[i]
  if idx1 == -1:
    continue
  for j in range(1,i):
    idx2, size2 = nums[j]
    if idx2 == -1 and size2 >= size1:
      nums.pop(j)
      nums[j:j] = [(idx1,size1),(-1,size2-size1)]
      nums[i+1] = (-1, size1)
      break
  #printNums(nums)

c = 0
position = 0
for i, (idx,size) in enumerate(nums):
  if idx == -1:
    position += size
  else:
    for _ in range(size):
      c += idx * position
      position += 1

print(c)