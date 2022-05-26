n=int(input())
for i in range(n):
  nums=int(input())
  l=list(map(int,input().split()))
  for i in range(nums):
    if len(l)==0 :
      break 
    maxitem=max(l)
    maxindex=l.index(maxitem)
    print(*l[maxindex:],end=" ")
    l=l[:maxindex]
  print()

  