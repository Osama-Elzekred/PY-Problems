n=int(input())
m=int(input())
l=[]
num=0
size=0
for i in range(n):
  l.append(int(input()))
l.sort(reverse=True)
for i in range(len(l)) :
  if size<m: 
    num+=1
    size+=l[i]
  if m==size : break 

print(num)