from typing import List, Tuple

f = open('inp.txt', 'r')

g = [[int(x) for x in r.strip()] for r in f.readlines()]

def search(g: List[List[int]], x: int, y: int, height: int) -> List[Tuple[int, int]]:
  if height == 10:
    return [(x, y)]
  directions = [(-1,0),(0,1),(1,0),(0,-1)]
  result = []
  for xOffset, yOffset in directions:
    nextX = x + xOffset
    nextY = y + yOffset
    if 0 <= nextX < len(g[0]) and 0 <= nextY < len(g) and g[nextY][nextX] == height:
      result += search(g, nextX, nextY, height + 1)
  return result

part1 = 0
part2 = 0
for i, row in enumerate(g):
  for j, x in enumerate(row):
    if x == 0:
      result = search(g, j, i, 1)
      part1 += len(set(result))
      part2 += len(result)
print(part1, part2)