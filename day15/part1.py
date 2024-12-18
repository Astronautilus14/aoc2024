grid, moves = open('inp.txt', 'r').read().split('\n\n')
grid = list(map(list, grid.split('\n')))

x,y=-1,-1
for i, row in enumerate(grid):
  for j, cell in enumerate(row):
    if cell == '@':
      x, y = j, i
      break

for move in moves:
  if move == '\n':
    continue

  xdir, ydir = 0, 0
  nx, ny = -1, -1
  if move == '>':
    nx, ny = x+1, y
    xdir = 1
  elif move == '<':
    nx, ny = x-1, y
    xdir = -1
  elif move == '^':
    nx, ny = x, y-1
    ydir = -1
  else:
    nx, ny = x, y+1
    ydir = 1
    
  if grid[ny][nx] == '.':
    grid[y][x] = '.'
    grid[ny][nx] = '@'
    x,y=nx,ny
    continue
  if grid[ny][nx] == '#':
    continue

  nnx, nny = nx, ny
  while nny in range(len(grid)) and nnx in range(len(grid[0])) and grid[nny][nnx] == 'O':
    nnx += xdir
    nny += ydir

  if grid[nny][nnx] == '.':
    grid[nny][nnx] = 'O'
    grid[ny][nx] = '@'
    grid[y][x] = '.'
    x, y = nx, ny

res = 0
for i, row in enumerate(grid):
  for j, cell in enumerate(row):
    if cell == 'O':
      res += 100 * i + j

print(res)