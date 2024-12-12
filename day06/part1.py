f = open('inp.txt', 'r')

directions = [(0,-1),(1,0),(0,1),(-1,0)]
# x, y, dir (0-3)
position = (0,0,0)

# 0: never visited, 1: visited, 3: object
g = []

for i, l in enumerate(f.readlines()):
  row = []
  for j, x in enumerate(l.strip()):
    row.append(0 if x == '.' else 1 if x == '^' else 3)
    if x == '^':
      position = (j, i, 0)
  g.append(row)

m = len(g[0])
n = len(g)

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
  position = (nextX, nextY, dir)

c = 0
for row in g:
  for x in row:
    if x == 1:
      c += 1

print(c)
