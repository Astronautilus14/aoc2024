import re

f = open('inp.txt', 'r')
g = [x.strip() for x in f.readlines()]
sum = 0

def checkLine(line: str):
  return len(re.findall('XMAS', line))

def computeDiagonals(grid):
  diagonals1 = ['' for _ in grid]
  diagonals2 = ['' for _ in grid[0]]
  for i, line in enumerate(grid):
    for j, char in enumerate(line):
      if i-j >= 0:
        diagonals1[i-j] += char
      else:
        diagonals2[j-i] += char
  return diagonals1 + diagonals2

for line in g:
  sum += checkLine(line)
  sum += checkLine(line[::-1])

rotated = [list(x) for x in list(zip(*g[::-1]))]

for line in rotated:
  sum += checkLine("".join(line))
  sum += checkLine("".join(line[::-1]))

for diagonal in computeDiagonals(g):
  sum += checkLine(diagonal)
  sum += checkLine(diagonal[::-1])

for diagonal in computeDiagonals(rotated):
  sum += checkLine(diagonal)
  sum += checkLine(diagonal[::-1])

print(sum)