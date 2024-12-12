f = open('inp.txt', 'r')
nums = [int(x) for x in f.readline()]

#nums = [int(x) for x in "2333133121414131402"]

left = 1 # Skip first as ID 0 does nothing to end result
position = nums[0]
right = len(nums) - 2 + (len(nums) % 2) # Right most file
c = 0

while left <= right:
  if left % 2 == 1:
    # Free space
    available  = nums[left]
    needed = nums[right]
    if available == needed:
      # for _ in range(available):
      #   c += right // 2 * position
      #   position += 1
      c += (available * (right // 2) * (available + 2 * position - 1)) // 2
      position += available
      left += 1
      right -= 2
    elif available > needed:
      # for _ in range(needed):
      #   c += right // 2 * position
      #   position += 1
      c += (needed * (right // 2) * (needed + 2 * position - 1)) // 2
      position += needed
      right -= 2
      nums[left] -= needed
    else:
      # for _ in range(available):
      #   c += right // 2 * position
      #   position += 1
      c += (available * (right // 2) * (available + 2 * position - 1)) // 2
      position += available
      left += 1
      nums[right] -= available
  else:
    # File
    # for _ in range(nums[left]):
    #   c += left // 2 * position
    #   position += 1
    c += (nums[left] * (left // 2) * (nums[left] + 2 * position - 1)) // 2
    position += nums[left]
    left += 1
  
print(c)