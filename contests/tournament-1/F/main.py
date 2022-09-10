n = int(input())

for _ in range(n):
  m, *a = input()

  if a.count('1') > 1:
    out = 'X'
  elif m == '1' or a.count('0') == 3:
    out = '0'
  else:
    out = '1'

  print(out)