l=[int(x) for x in input().split()]
min=l[0]
for i in range(len(l)):
  if min>l[i]:min=l[i]
print (min)