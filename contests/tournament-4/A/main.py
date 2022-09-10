def verifica(sequencia, subsequencia):
  for palavra in subsequencia:
    print(palavra, sequencia)
    if palavra in sequencia:
       return True
  return False


n = int(input())
for i in range(n):
  sequencia = input()
  q = int(input())
  for j in range(q):
    subsequencia = input()
    if verifica(sequencia, subsequencia):
      print("Yes")

    else:
      print("No")
