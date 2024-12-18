# f = open('inp.txt', 'r')

# a = int(f.readline().strip().split(': ')[1])
# f.readline()
# b = int(f.readline().strip().split(': ')[1])
# c = int(f.readline().strip().split(': ')[1])
# f.readline()
# program = list(map(int,f.readline().strip().split(': ')[1].split(',')))

# target = [2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0]

# def run(a: int):
#   b = 0
#   for i in range(16):
#     b = (a%8) ^ (a >> ((a%8) ^ 1)) ^ 5
#     a = a >> 3
#     out = b%8
#     if out != target[i]:
#       return False
#   return True

# # print(run(30553366))

# for a in range(35196300000000, 281474976710656):
#   if a % 100000000 == 0:
#     print('a:', a, f'{(a-35196300000000)/281474976710656}%')

#   if run(a):
#     print('!!!!!!')
#     print(a)
#     print('!!!!!!')
#     break

for a in range(800):
  b = (a%8) ^ (a >> ((a%8) ^ 1)) ^ 5
  if b%8 == 2:
    print(a % 8)