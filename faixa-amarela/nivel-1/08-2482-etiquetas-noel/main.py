n = int(input())

dict = {}

for i in range(n):
  idioma = input()
  frase = input()

  dict[idioma] = frase

m = int(input())

for i in range(m):
  nome = input()
  idioma = input()

  print(nome)
  print(dict[idioma])
  print()