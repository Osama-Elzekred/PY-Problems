def solve():
  n=int(input())
  l = list(map(int, input().split()))
  for i in range(len(l)) :
    for j in range(len(l)):
     if j==i : continue
     z=l[i]-l[j]
     for k in range(len(l)):
       if k==i or k==j: continue
       if l[k]==z  :
         print(f"{i+1} {j+1} {k+1}")
         return 1
  print("-1")
solve()
