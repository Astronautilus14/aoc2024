from functools import cache


patterns, lines = open('inp.txt','r').read().split('\n\n')
patterns = patterns.split(', ')
lines = lines.split('\n')

@cache
def recBackTracking(goal: str):
  global patterns

  if goal == '':
    return 1

  c = 0
  for pattern in patterns:
    if goal.startswith(pattern):
      c += recBackTracking(goal[len(pattern):])
      
  return c


s1 = 0
s2 = 0
for l in lines:
  res = recBackTracking(l)
  s1 += 1 if res > 0 else 0
  s2 += res

print('Part 1:', s1)
print('Part 2:', s2)

