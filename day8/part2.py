f = open('inp.txt', 'r')
g = {}
lines = f.readlines()
locations = set()
for i, l in enumerate(lines):
  l = l.strip()
  for j, x in enumerate(l):
    if x.isalnum():
      if x in g:
        for xPos, yPos in g[x]:
          dX = xPos - j
          dY = yPos - i

          multiplier = 0
          fX, fY = xPos, yPos
          while 0 <= fX < len(l) and 0 <= fY < len(lines):
            locations.add((fX,fY))
            fX = xPos + multiplier * dX
            fY = yPos + multiplier * dY
            multiplier += 1

          multiplier = 0
          sX, sY = xPos, yPos
          while 0 <= sX < len(l) and 0 <= sY < len(lines):
            locations.add((sX,sY))
            sX = xPos - multiplier * dX
            sY = yPos - multiplier * dY
            multiplier += 1

          # print('dX', dX, 'dY', dY)
          # print('Known pos', xPos, yPos)
          # print('New pos', j, i)
          # print('First attempt', fX, fY)
          # print('Second attept', sX, sY, '\n')
        g[x].append((j,i))
      else:
        g[x] = [(j,i)]
#print(locations)

# g = [list(x.strip()) for x in lines]
#print("\n".join("".join(x) + f" {i}" for i, x in enumerate(g)))
# for x, y in locations:
  # print(x, y)
  # g[y][x] = '#'
# print("\n".join("".join(x) + f" {i}" for i, x in enumerate(g)))

print(len(locations))