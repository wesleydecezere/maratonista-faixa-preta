def byLen(e):
  return len(e)

while True:
    sOriginal = input()

    if(sOriginal == '.'):
      break
  
    strs = sOriginal.split(' ')
    strs.sort()
 
    words = []
    group = []

    if len(strs) > 1:
      for i in range(len(strs) - 1):
        s1 = strs[i]
        s2 = strs[i+1]
  
        group.append(s1)
  
        word = ''
        
        if i == len(strs)-2:
          if s1[0] == s2[0]:
            group.append(s2)
          else:
            words.append(s2)
            sOriginal = sOriginal.replace(s2, s2[0]+'.')
        
        if s1[0] != s2[0]:
          group.sort(reverse=True, key=byLen)        
  
          if len(group) > 1:
            # atribui peso a cada palavra (len * ocorrencias)
            mappedGroup = {}
            
            for w in group:
              mappedGroup[w] = strs.count(w) * len(w)
            
            sorted(mappedGroup.items(), key=lambda x: x[1], reverse=True)
            
            # seleciona a palavra de maior peso
            word = list(mappedGroup.keys())[0]
          else:        
            word = group[0]
  
          group = []
  
          if len(word) > 2:
            words.append(word)
            sOriginal = sOriginal.replace(word, word[0]+'.')
  
        # for w in words:
        #   sOriginal = sOriginal.replace(w, w[0]+'.')

    elif len(strs[0]) > 2:
      words.append(strs[0])
      sOriginal = sOriginal.replace(words[0], words[0][0]+'.')
  
    print(sOriginal)
    print(len(words))
  
    words.sort()

    for w in words:
      print('%s. = %s' % (w[0], w))