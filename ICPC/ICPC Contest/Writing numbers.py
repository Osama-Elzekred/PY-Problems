L,R=[int(x) for x in input().split()]
flag=0
if L%2==0 : 
  print(L,end=" ")
  L=L+1
for i in range(L,R):
  if flag :
      flag=0 
      continue
  if i%2!=0 and i+1<=R:     
    print(i+1,end=" ")
    print(i,end=" ")
    flag=1
if R&1 :print(R)
 