str=input()
l=[]

for i in range(len(str)):
  x=ord(str[i])
  if x == 122 : x=96 
  l.append(chr(x+1))
print(''.join(l))