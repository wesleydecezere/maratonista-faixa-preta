# le n
# para i de 0 a n:
    # le linha
    # mtx.append(linha)
    # somaLinha[i] = soma(linha)

    # para j de 0 a n:
        # somaColuna[j] += linha[j]

# soma = [somaLinha, somaColuna]
# para i de 0 a 2:

    # (a, b) = set of soma[i]
    # nA = conta a in soma[i]
    # nB = conta b in soma[i]

    # idx[i] = indexOf(nA > nB ? a : b)

# substituto = mtx[idx[0]][idx[1]]
# (somaCorreta, somaErrada) = nA > nB ? (a,b) : (b,a)
# substituido = abs(substituto - abs(somaCorreta - somaErrada))
