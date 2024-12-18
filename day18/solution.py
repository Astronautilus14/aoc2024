width = height = 71
bytes = 1024
g = [[0 for _ in range(width)] for _ in range(height)]

def dijkstra():
  global g

  distances = {
    (0, 0): 0
  }
  # paths = {}
  queue = [(0, 0)]

  while len(queue) > 0:
    # print(queue)
    curr = queue.pop(0)
    x, y = curr

    neighbours = []
    directions = [(1,0), (0,1), (-1, 0), (0,-1)]
    for dx, dy in directions:
      nx, ny = x + dx, y + dy

      if nx == width-1 and ny == height-1:
        return distances[curr] + 1

      if ny in range(height) and nx in range(width) and g[ny][nx] == 0:
        neighbours.append((nx, ny))

    # print(curr, neighbours)

    for neighbour in neighbours:
      dist = distances[curr] + 1

      if (neighbour in distances and distances[neighbour] > dist) or not neighbour in distances:
          distances[neighbour] = dist
          #paths[neighbour] = paths[curr] + [neighbour]
          for i, v in enumerate(queue):
            if dist <= distances[v]:
              queue[i:i] = [neighbour]
              break
          else:
            queue.append(neighbour)
  return False

lines = open('inp.txt', 'r').read().split('\n')


for l in lines[:bytes]:
  x,y = l.split(',')
  g[int(y)][int(x)] = 1

print('Part 1:', dijkstra())

g = [[0 for _ in range(width)] for _ in range(height)]

for i, l in enumerate(lines):
  x,y = l.split(',')
  g[int(y)][int(x)] = 1
  if i < bytes:
    continue
  if dijkstra() == False:
    print('Part 2:', f"{x},{y}")
    break