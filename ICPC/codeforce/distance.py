import math
n= int(input())
x1=0
y1=0
while n>0:
  x,y=[int(z) for z in input().split()]
  temp=math.sqrt((x-x1)**2+(y-y1)**2)
  if(x==y==0):print ("0")
  elif(math.floor(temp)!=math.ceil(temp)):
    print("2")
  else: print ("1")
  n-=1


  