fib_num = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,1597,2584,4181,6765,10946,17711]
for i in range(int(input())):
  num = int(input())
  bin_repr = [0 for x in range(fib_num)]
  temp = fib_num.copy()
  temp.reverse()
  for fib in temp:
    if fib > num:
      continue
    elif (num%fib) in temp:
      bin_repr[temp.index(num%fib)] = 1
      bin_repr[temp.index(fib)] = 1
      break
    else:
      num -= fib
      bin_repr[temp.index(fib)] = 1
      