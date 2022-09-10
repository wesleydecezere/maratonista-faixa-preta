azulejos = []

def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b) 


def find_azulejos(num,div):
  num_tiles = num//div
  for i in range(num_tiles):
    azulejos.append(div*(i+1))
 
while True:
  azulejos = []
  n,a,b = input().split()
  n=int(n)
  a=int(a)
  b=int(b)
  gdc = hcfnaive(a,b)
  if n == 0 and a == 0 and b == 0:
    break
  else:
    if max(a,b)%min(a,b)==0:
      print(find_azulejos(n,min(a,b)))
    else:
      if gdc == 1:
        print((n//a)+(n//b)-1)
      else:
        pass
    find_azulejos(int(n),int(a))
    find_azulejos(int(n),int(b))