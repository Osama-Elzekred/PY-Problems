
import copy
def swap(l):
  
      temp=0
      minindex=l.index(min(l))
      if minindex != temp :
         l[temp],l[minindex] = l[minindex],l[temp]
         temp+=1
      else: 
        l2=l[1:]
        minitem2=min(l2)
        minindex2=l.index(minitem2)
        l[minindex2],l[1]=l[1],l[minitem2]
        


        # l2=l.copy()
        # l2.remove(min(l2))
        # minitem2=min(l2)
        # minindex2=l.index(minitem2)


def solve():
  n=int(input())
  for _ in range(n):
    str=input()
   
    l=list(map(int,str))
    swap(l)
    


          
        




     return str[0]
      
  
