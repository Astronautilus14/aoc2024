f = open('./sample.txt', 'r')

sum = 0
for line in f.readlines():
  levels = list(map(int, line.split(' ')))
  isIncreasing = levels[0] < levels[1]
  for i, (curr, next) in enumerate(zip(levels, levels[1:])):
    if isIncreasing: 
      if curr > next:
        break
    elif curr < next:
      break
    if abs(next - curr) > 3 or next == curr:
      break
  else:
    sum += 1
    continue
  
  for i in range(len(levels)):
    newLevels = [l for j, l in enumerate(levels) if j != i]
    isIncreasing = newLevels[0] < newLevels[1]
    for curr, next in zip(newLevels, newLevels[1:]):
      if isIncreasing: 
        if curr > next:
          break
      elif curr < next:
        break
      if abs(next - curr) > 3 or next == curr:
        break
    else:
      sum += 1
      break

print(sum)
   
