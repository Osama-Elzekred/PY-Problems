n=int(input())
for _ in range(n):
  t=int(input())
  max=0
  for i in range(t):
    n,m=[int(x) for x in input().split()]
    if n>= m: max+=1
  print(max)
