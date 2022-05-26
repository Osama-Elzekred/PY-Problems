from collections import Counter
money=0
shoes_num =int(input())
shoes=[int(item) for item in (input().split())]
shoe_count=Counter(shoes)
for _ in range(int(input())):
  x,y= map(int, input().split()) 
  if shoe_count[x] > 0 :
     money+=y
     shoe_count[x]-=1
print(money)
  
     