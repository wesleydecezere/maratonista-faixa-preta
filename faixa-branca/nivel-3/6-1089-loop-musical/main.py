while True:
    N = int(input())
    if N==0:
        break
    picos = 0
    values = input().split()
    for i in range(N):
      if i+1==N:
        if int(values[i])<int(values[0]) and int(values[i])<int(values[i-1]):
          picos += 1
      else:
        if int(values[i])<int(values[i+1]) and int(values[i])<int(values[i-1]):
          picos += 1
    picos = picos*2
    print(picos)