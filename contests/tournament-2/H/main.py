teclado = {
  'A': 2, 'B': 2, 'C': 2,
  'D': 3, 'E':3, 'F':3,
  'G':4,'H':4,'I':4,
  'J':5,'K':5,'L':5,
  'M':6,'N':6,'O':6,
  'P':7,'Q':7,'R':7,'S':7,
  'T':8,'U':8,'V':8,
  'W':9,'X':9,'Y':9,'Z':9,
  '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9
}

while True:
  try:
    number = list(input())
    real_number=''
    for i in number:
      if i == "*" or i=='#':
        real_number = real_number + i
      elif i.upper() in teclado:
        real_number = real_number + str(teclado[i.upper()])
      else:
        pass
    print(real_number)
  except EOFError:
    break