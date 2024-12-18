robots = [[tuple(map(int, x.split('=')[1].split(','))) for x in line.split(' ')] for line in open('inp.txt').read().split('\n')]

width = 101
height = 103

for t in range(100000000):
  seen = set()
  for i, ((xPos, yPos), (xVel, yVel)) in enumerate(robots):
    nx = (xPos + xVel) % width
    ny = (yPos + yVel) % height
    robots[i][0] = (nx, ny)
    seen.add((nx, ny))

  if len(robots) == len(seen):
    gc = [[0 for _ in range(width)] for _ in range(height)]
    for (x,y), _ in robots:
      gc[y][x] += 1
    print("\n".join("".join(['.' if x == 0 else '#' for x in l]) for l in gc))
    print('t:', t+1, '\n\n')
    break

quadrants = [[0,0],[0,0]]

for (xPos, yPos), _ in robots:
  if xPos == width // 2 or yPos == height // 2:
    continue
  
  xCord = 0 if xPos <= width // 2 else 1
  yCord = 0 if yPos <= height // 2 else 1
  quadrants[xCord][yCord] += 1

res = 1
for r in quadrants:
  for q in r:
    if q == 0:
      continue
    res *= q
print(res)
  


# 219801600 too high
#  88046400 too low