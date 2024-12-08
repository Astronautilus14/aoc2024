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

          fX = xPos + dX
          fY = yPos + dY
          if 0 <= fX < len(l) and 0 <= fY < len(lines):
            locations.add((fX,fY))

          sX = xPos - 2 * dX
          sY = yPos - 2 * dY
          if 0 <= sX < len(l) and 0 <= sY < len(lines):
            locations.add((sX,sY))

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