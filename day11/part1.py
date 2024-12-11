from functools import cache

stones = [2, 72, 8949, 0, 981038, 86311, 246, 7636740] # input
# stones = [125, 17] # sample

@cache
def calculateSize(stone, depth):
  if depth == 0:
    return 1
  
  if stone == 0:
      return calculateSize(1, depth-1)
  
  string = str(stone)
  if len(string) % 2 == 0:
    idx = len(string) // 2
    return calculateSize(int(string[:idx]), depth-1) + calculateSize(int(string[idx:]), depth-1)
  
  return calculateSize(stone * 2024, depth - 1)

res = 0
for i, stone in enumerate(stones, 1):
  res += calculateSize(stone, 75)

print(res)