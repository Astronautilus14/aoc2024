f = open('inp.txt', 'r')
g = [x.strip() for x in f.readlines()]
sum = 0

for i, line in enumerate(g[1:-1]):
  for j, char in enumerate(line[1:-1]):
    if char == 'A':
      c = 0
      for x, y in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        pos1 = g[i+1+x][j+1+y]
        pos2 = g[i+1+x*-1][j+1+y*-1]
        if pos1 == 'M' and pos2 == 'S':
          c += 1
      if c > 1:
        sum += 1

print(sum)