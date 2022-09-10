n, q = [int(x) for x in input().split()]

nome = ['']

for _ in range(n-1):
  p, c = input().split()
  p = int(p)

  nome.append(nome[p-1] + c)

# print(nome)

for _ in range(q):
  i, j = [int(x) for x in input().split()]

  a = nome[i-1]
  b = nome[j-1]

  m = min(a, b)

  for k in range(len(m)-1, -1, -1):
    if a[k] != b[k]:
      print(k)
      break



  