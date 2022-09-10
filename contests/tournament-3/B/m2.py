import re

# nao funciona pro algoritmo abaixo porque teria que testar todas as combinações
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

while True:
    m = int(input())
    if m == 0:
        break
    
    s = input()
    uniques = unique(s)
    lens = []

    for i in range(len(uniques) - (m-1)):
      seq = uniques[i:i+m]
      seq = ''.join(seq)
      
      pattern = "[{}]+".format(seq)

      print(seq, pattern)
      
      subs = re.findall(pattern, s)
      lens.append(len(max(subs)))    
 
    # print(s, lens)
    print(max(lens))