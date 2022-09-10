n = int(input())
line = input().split()

while (n > 1):
  nextLine = []
  n = n - 1

  for i in range(n):
    nextLine.append('1' if line[i] == line[i+1] else '-1')

  line = nextLine

print('preta' if line[0] == '1' else 'branca')