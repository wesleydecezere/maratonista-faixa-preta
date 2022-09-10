n, permutacoes = [int(x) for x in input().split()]
chave = [int(x) for x in input().split()]

seqs = []

while True:
  chaveCopia = chave.copy()
  seq = [min(chave)]
  i = 0

  while True:
    # print(seq, chave, chaveCopia)
    nextIdx = chave.index(seq[i])
    
    seq.append(nextIdx + 1)
    chaveCopia[nextIdx] = n+1
    
    if i>0 and seq[0] == seq[-1]:
      chave = chaveCopia
      break
      
    i += 1

  seqs.append(seq)
  
  if len(set(chave)) == 1 and chave[0] == n+1:
    break

print(seqs)

for seq in seqs:
  
  
      

  
