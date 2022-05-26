l=[]
flag=0
n=int(input())
for i in range(n):
  N,M=[int(x) for x in input().split()]
  for j in range(N):
    I,J=[int(x) for x in input().split()]
    if (I,J) in l :
      flag=1 
    l.append((I,J))
  if (flag==1):print("YES")
  else:print("NO")
# print(l)
