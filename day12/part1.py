from typing import List, Set, Tuple

g = [list(l.strip()) for l in open('inp.txt').readlines()]

directions = [(-1,0), (0,1), (1,0), (0, -1)]
regions: List[Tuple[int, int]] = []

seen: Set[Tuple[int, int]] = set()
def floodfill(x: int, y: int) -> List[Tuple[int, int]]:
  seen.add((x, y))
  region = [(x, y)]
  for xdir, ydir in directions:
    x2, y2 = x + xdir, y + ydir
    if (x2, y2) not in seen and x2 in range(len(g[0])) and y2 in range(len(g)) and g[y2][x2] == g[y][x]:
      region += floodfill(x2, y2)
  return region

for i, row in enumerate(g):
  for j, cell in enumerate(row):
    if (j,i) in seen:
      continue
    regions.append(floodfill(j,i))

res = 0
for region in regions:
  area = len(region)
  perimeter = 0
  for x, y in region:
    c = 4
    for xdir, ydir in directions:
      if (x+xdir, y+ydir) in region:
        c -= 1
    perimeter += c
  res += area * perimeter

print(res)