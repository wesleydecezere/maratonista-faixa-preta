import re

while (1):
    l, c, p = input().split()
    l = int(l)
    c = int(c)
    p = int(p) - 1

    if l == 0 and c == 0 and p == -1:
        break

    m = []
    e = False

    for i in range(l):
        m.append(input().split())

    for i in range(l):
        # se já esotourou
        if e:
          break

        # pega a difetença entre os ventiladores
          # 1 : slice à esquerda e à direita de p
          # 2a: iterar ate ecnontrar m[i][j] != 0
          # 2b: encontrar primeiro nro != 0, da direção do balão à extremidade

        mLeft = ''.join(m[i][:p][::-1])
        mRight = ''.join(m[i][p:])

        dLeft = re.findall("[1-9]", mLeft)[0]
        dRight = re.findall("[1-9]", mRight)[0]

        diff = int(dLeft) - int(dRight)
        
        # enquanto restar deslocamento
          # desloca uma unidade
          # se a nova posição tem ventilador, finaliza

        while (diff != 0):
            if diff > 0:
                p += 1
                diff -= 1
            elif diff < 0:
                p -= 1
                diff += 1

            if m[i][p] != '0':
                e = True
                break

    if (e):
        print('BOOM', i + 1, p + 1)
    else:
        print('OUT', p + 1)
