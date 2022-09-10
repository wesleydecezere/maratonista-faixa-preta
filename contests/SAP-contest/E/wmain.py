# le n
# calcula raiz de n
# se raiz inteira -> imprime raiz, raiz
# se nao
# para i de int(raiz) a 0:
# divide n por i
# se resultado intero:
# imprime i, resultado
n = int(input())

r = pow(n, 1 / 2)

if r == int(r):
    print(int(r), int(r))
else:
    for i in range(int(r) + 1, 0, -1):
        div = n / i
        if div == int(div):
            small = min(int(div), i)
            big = max(int(div), i)
                    
            print(small, big)

            break

            # exp = 2
            # j = i
            # while j > 0:
            #   div = n / j
            #   if div == int(div):
            #     print(j, int(div))
            #     break

            #   j -= disc

            # if j > 0:
            #   print(i, int(div))
            #   break
