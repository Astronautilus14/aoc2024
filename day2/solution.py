f = open('./inp.txt', 'r')

sum = 0
for line in f.readlines():
  levels = list(map(int, line.split(' ')))
  isIncreasing = levels[0] < levels[1]
  for level, next in zip(levels, levels[1:]):
    if isIncreasing and level > next:
        break
    elif level < next:
      break
    if abs(next - level) > 3 or next == level:
      break
  else:
    sum += 1

print(sum)
   
