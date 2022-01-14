l, c, p = input().split()
l = int(l)
c = int(c)
p = int(p) - 1

m = []
v = []
e = False

while (1):
    if l == 0 and c == 0 and p == 0:
        break

    for i in range(l):
        m.append(input().split())
        print(m)
        v.append(int(m[i][0]) - int(m[i][c - 1]))

    for i in range(l):
        for j in range(c):
            if not e and j == p:
                # calcula a difetença entre os ventiladores
                # desloca o balão
                # uma unidade
                # verfica se a nova posição tem ventilador
                while (v[i] != 0):
                    if v[i] > 0:
                        p += 1
                    if v[i] < 0:
                        p -= 1

                    if m[i][p] != '0':
                        e = True
                        break

    if (e):
        print('BOOM', i, j)
    else:
        print('OUT', p + 1)

print(m)
