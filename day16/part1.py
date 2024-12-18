g = [list(line.strip()) for line in open('inp.txt', 'r').readlines()]

directions = [(1,0), (0,1), (-1, 0), (0,-1)]

for i, line in enumerate(g):
  for j, cell in enumerate(line):
    if cell == 'S':
      start = (j, i, 0)
      break

distances = {
  start: 0
}
# paths = {}
queue = [start]

while len(queue) > 0:
  curr = queue.pop(0)
  x, y, dir = curr
  xdir, ydir = directions[dir]

  neighbours = []
  nx, ny = x + xdir, y + ydir

  if ny in range(len(g)) and nx in range(len(g[0])):
    if g[ny][nx] == 'E':
      print(distances[curr] + 1)
      break
    if g[ny][nx] == '.':
      neighbours.append(((nx, ny, dir), 1))

  neighbours.append(((x,y,(dir + 1) % 4), 1000))
  neighbours.append(((x, y, (dir - 1) % 4), 1000))

  for neighbour, edge in neighbours:
    dist = distances[curr] + edge
    if (neighbour in distances and distances[neighbour] > dist) or not neighbour in distances:
        distances[neighbour] = dist
        #paths[neighbour] = paths[curr] + [neighbour]
        for i, v in enumerate(queue):
          if dist <= distances[v]:
            queue[i:i] = [neighbour]
            break
        else:
          queue.append(neighbour)