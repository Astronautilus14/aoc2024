def printGrid(grid):
  for row in grid:
    s = ""
    for x in row:
      s += '.' if x == 0 else '#' if x == 3 else 'X'
    print(s)

def deepCopy(grid):
  return [[x for x in r] for r in grid]

f = open('inp.txt', 'r')

# x, y, dir (0-3)
directions = [(0,-1),(1,0),(0,1),(-1,0)]
position = (0,0,0)
originalPosition = position

# 0: never visited, 1: visited, 3: object
g = []

for i, l in enumerate(f.readlines()):
  row = []
  for j, x in enumerate(l.strip()):
    row.append(0 if x == '.' else 1 if x == '^' else 3)
    if x == '^':
      position = (j, i, 0)
      originalPosition = position
  g.append(row)

m = len(g[0])
n = len(g)
originalG = deepCopy(g)

potentialPositions = set()

while True:
  x, y, dir = position
  xDir, yDir = directions[dir]
  nextX, nextY = (x + xDir, y + yDir)
  if not (0 <= nextX < m and 0 <= nextY < n):
    # Off the map
    break
  if g[nextY][nextX] == 3:
    # turn to the right
    position = (x, y, (dir + 1) % 4)
    continue

  g[nextY][nextX] = 1
  potentialPositions.add((nextX, nextY))
  position = (nextX, nextY, dir)

obstructions = set()

for obstuction in potentialPositions:
  if obstuction[0] == originalPosition[0] and obstuction[1] == originalPosition[1]:
    continue
  
  currentGrid = deepCopy(originalG)
  currentGrid[obstuction[1]][obstuction[0]] = 3
  position = originalPosition
  seenPositions = set()


  while True:
    # print(position, seenPositions, '\n')
    # printGrid(g)
    if position in seenPositions:
      obstructions.add(obstuction)
      break
    seenPositions.add(position)
    x, y, dir = position
    xDir, yDir = directions[dir]
    nextX, nextY = (x + xDir, y + yDir)
    if not (0 <= nextX < m and 0 <= nextY < n):
      # Off the map
      break
    if currentGrid[nextY][nextX] == 3:
      # turn to the right
      position = (x, y, (dir + 1) % 4)
      continue

    currentGrid[nextY][nextX] = 1
    position = (nextX, nextY, dir)

print(len(obstructions))