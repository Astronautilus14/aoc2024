f = open('inp.txt', 'r')

a = int(f.readline().strip().split(': ')[1])
b = int(f.readline().strip().split(': ')[1])
c = int(f.readline().strip().split(': ')[1])
f.readline()
program = list(map(int,f.readline().strip().split(': ')[1].split(',')))
ip = 0
output = []

def combo(operand: int) -> int:
  if operand in range(4):
    return operand
  if operand == 4:
    return a
  if operand == 5:
    return b
  if operand == 6:
    return c
  raise Exception(f'Unknown combo operand: {operand}')

while ip < len(program)-1:
  opcode = program[ip]
  operand = program[ip+1]

  if opcode == 0:
    a = a // (2**combo(operand))
  elif opcode == 1:
    b = b ^ operand
  elif opcode == 2:
    b = combo(operand) % 8
  elif opcode == 3:
    if a != 0:
      ip = operand - 2
  elif opcode == 4:
    b = b ^ c
  elif opcode == 5:
    output.append(str(combo(operand) % 8))
  elif opcode == 6:
    b = a // (2**combo(operand))
  elif opcode == 7:
    c = a // (2**combo(operand))

  ip += 2

print(",".join(output))