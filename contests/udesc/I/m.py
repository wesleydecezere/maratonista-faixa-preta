s = input()

s = s.replace('(', '')
s = s.replace(')', '')
clausulas = s.split('&')
kla = []

for c in clausulas:
  while '~' in c:
    i = c.index('~')
    letra = c[i+1]
    c = c.replace('~' + letra, '', 1)
    c = c.replace(letra, '', 1)

  kla.append(c)
print(kla)

literais = [c.split('|') for c in kla]
maxs = [len(max(x)) for x in literais]
mins = [len(min(x)) if len(min(x)) != 0 else 1 for x in literais]

print(literais)
print(maxs)

maximo = sum(maxs)  
minimo = sum(mins)
print(maximo, minimo)

if (maximo == minimo):
  if maximo == 1:
    print('SAT-1') 
  if maximo == 3:
    if max(maxs) == 1:
      print('SAT-1')
    else:
      print("SAT-3")
  else:
    print('SAT-2')
else:
  print('SAT-2')

# print(re.sub("\([a-z]([a-z|\|]*)-[a-z]\)", "\($1\)", s, 3, 3))