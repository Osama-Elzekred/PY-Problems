x =int(input())
l = [*range(0,11)]
l2=[]
for i in range(x): 
 if (i == x//2 and x%2==0):
  break
 l2.append(l[x-i-1])
 if (i == x//2 and x%2!=0):
  break
 l2.append(l[i]) 
print (l2)

# def solve(l,temp):
#   if temp == l.__len__()//2:
#     return 0
#   temp2=l[temp]
#   l[temp]=l[l.__len__()-temp2-1] 
#   temp+=1
#   solve(l,temp)
  
   

# x =int(input())
# l = [*range(0,11)]
# l.reverse()
# temp=0
# solve(l,temp)
# print(l)