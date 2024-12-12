f = open('inp.txt', 'r')

rules = {}
updates = []

for l in f:
  if l.strip() == '':
    break

  fst, snd = map(int, l.strip().split('|'))
  if snd in rules.keys():
    rules[snd] += [fst]
  else:
    rules[snd] = [fst]

for l in f:
  updates.append([int(x) for x in l.strip().split(',')])

sum1 = 0
incorrect = []

for update in updates:
  for i, x in enumerate(update):
    for rule in rules.get(x, []):
      for y in update[i:]:
        if rule == y:
          break
      else:
        continue
      break
    else:
      continue
    break
  else:
    sum1 += update[len(update) // 2]
    continue
  incorrect.append(update)

print('Part 1: ', sum1)

sum2 = 0

for update in incorrect:
  # Sort
  while True:
    swapped = False
    for i, (left, right) in enumerate(zip(update, update[1:])):
      if right in rules.get(left, []):
        swapped = True
        update[i] = right
        update[i+1] = left
    if not swapped:
      break
  sum2 += update[len(update) // 2]

print("Part 2: ", sum2)