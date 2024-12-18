from collections import defaultdict

g = [list(line.strip()) for line in open('inp.txt', 'r').readlines()]

directions = [(1,0), (0,1), (-1, 0), (0,-1)]

visited = set()
altpaths = defaultdict(list)
seenPaths = set()
def addAlternatives(p):
  for x,y,dir in p:
    visited.add((x,y))
    if (x,y,dir) in seenPaths:
      continue
    seenPaths.add((x,y,dir))
    for path in altpaths[(x,y,dir)]:
      addAlternatives(path)

for i, line in enumerate(g):
  for j, cell in enumerate(line):
    if cell == 'S':
      start = (j, i, 0)
      break

distances = {
  start: 0
}
paths = {
  start: []
}
queue = [start]

while len(queue) > 0:
  curr = queue.pop(0)
  x, y, dir = curr
  xdir, ydir = directions[dir]

  neighbours = []
  nx, ny = x + xdir, y + ydir

  if ny in range(len(g)) and nx in range(len(g[0])):
    if g[ny][nx] == 'E':
      visited.add((nx,ny))
      addAlternatives(paths[curr])
      print(len(visited))
      break
    if g[ny][nx] == '.':
      neighbours.append(((nx, ny, dir), 1))

  neighbours.append(((x,y,(dir + 1) % 4), 1000))
  neighbours.append(((x, y, (dir - 1) % 4), 1000))

  for neighbour, edge in neighbours:
    dist = distances[curr] + edge

    if neighbour in distances and distances[neighbour] == dist:
      altpaths[neighbour].append(paths[curr] + [neighbour])

    if (neighbour in distances and distances[neighbour] > dist) or not neighbour in distances:
        distances[neighbour] = dist
        paths[neighbour] = paths[curr] + [neighbour]
        altpaths[neighbour].clear()
        for i, v in enumerate(queue):
          if dist <= distances[v]:
            queue[i:i] = [neighbour]
            break
        else:
          queue.append(neighbour)