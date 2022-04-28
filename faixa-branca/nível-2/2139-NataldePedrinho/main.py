t=[31,29,31,30,31,30,31,31,30,31,30]
while True:
 m_d=input().split(' ')
 m=int(m_d[0])
 d=int(m_d[1])
 if(m==12 and d==25):
   print("E natal!")
 elif(m==12 and d==24):
   print("E vespera de natal!")
 elif(m==12 and d>25):
   print("Ja passou!")
 else:
   
