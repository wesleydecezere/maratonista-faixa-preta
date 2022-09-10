words = list(input())
m = []
result = str()
for i in range(len(words)):
  if i%2 == 0:
    m.append(words[i])
  else:
    result = result + words[i]
m.reverse()
for i in m:
  result = result + i
print(result)