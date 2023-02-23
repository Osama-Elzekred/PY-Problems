x,y=[int(x) for x in input().split()]
p=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
total_toys=0
total_money=0
k=0
def increase():
 pass
def solve():
  for i in range(len(p)):
    total_money += p[i]+t[i]*k 
    if total_money<y:
      
      total_toys+=1
      total_money