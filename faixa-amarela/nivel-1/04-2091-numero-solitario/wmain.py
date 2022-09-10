while True:
  n = int(input())
  if n == 0:
    break
  
  numbers = input().split()
  distinctNumbers = set(numbers)

  for nb in distinctNumbers:
    qtd = numbers.count(nb)
    
    if qtd % 2 != 0:
      print(nb)
      break