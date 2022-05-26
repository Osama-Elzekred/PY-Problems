l,r=[int(x) for x in input().split()]
if l>0 and abs(r)==r or -abs(l)==l and r<0 :
  print(0)
elif -abs(l)==l and r>0 :
  x= min(abs(r),abs(l))
  print(x*2+1)
elif l==0 or r==0 :
  print(1)