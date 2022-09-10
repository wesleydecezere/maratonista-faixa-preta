while True:
  p=input().split(' ')
  x1=int(p[0])
  y1=int(p[1])
  x2=int(p[2])
  y2=int(p[3])
  if(x1==0 and y1==0 and x2==0 and y2==0):
    break 
  else:
    if(x2-x1==0 and y2-y1==0):
      print("0")
    elif(x2-x1==y2-y1 or x2-x1==y1-y2 or x2==x1 or y2==y1):
      print("1")    
    else:
      print("2")
      
  
  
  