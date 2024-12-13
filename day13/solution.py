machines = [x.split('\n') for x in open('inp.txt', 'r').read().split('\n\n')]

res = 0
res2 = 0
for i, machine in enumerate(machines):
  a, k = tuple(int(x.split('+')[1]) for x in machine[0].split(','))
  b, l = tuple(int(x.split('+')[1]) for x in machine[1].split(','))
  c, m = tuple(int(x.split('=')[1]) for x in machine[2].split(','))

  c2 = c + 10000000000000
  m2 = m + 10000000000000

  # a*x + b*y = c
  # k*x + l*y = m

  # y = (kc - am) / (kb - al)
  # x = (c - by) / a

  # Part 1
  t1, t2 = (k*c - a*m), (k*b - a*l)
  if t1 % t2 == 0:
    y = t1 // t2
    t3 = (c - b*y)
    if t3 % a == 0:
      x = t3 // a
      res += 3*x + y

  # Part 2
  t1, t2 = (k*c2 - a*m2), (k*b - a*l)
  if t1 % t2 == 0:
    y = t1 // t2
    t3 = (c2 - b*y)
    if t3 % a == 0:
      x = t3 // a
      res2 += 3*x + y

print('Part 1:', res)
print('Part 2:', res2)

# 875318608908 too low