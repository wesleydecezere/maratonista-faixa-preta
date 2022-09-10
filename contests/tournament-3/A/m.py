i = 1

while True:
  try:
    r, l, w = [int(x) for x in input().split()]
    
    diametro = (2 * r)**2
    # diagonal da pizza deve ser igual ao diâmetro
    diagonal = l**2 + w**2

    # print(i, diametro, diagonal)
    
    if diametro < diagonal:
      print('Pizza {} does not fit on the table.'.format(i))
    else:
      print('Pizza {} fits on the table.'.format(i))
  
    i += 1

  except:
    break