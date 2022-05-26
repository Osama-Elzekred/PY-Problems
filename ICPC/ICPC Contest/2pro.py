def  sub_lists (l,n):
    max=0
    temp2=0
    for i in range(len(l) + 1):
      
      if i+n< len(l) + 1:
        temp=l[i]^l[i+1]^l[i+2]
        if max<temp :
          max=temp 
          # print(max) 
      else :
        temp2=abs(i-n)
        temp=l[temp2]^l[temp2+1]^l[temp2+2]
        if max<temp :
          max=temp 
       
    return max
  
# driver code
# n=int(input())
l1 = [3,7,5,9,8]
print(sub_lists(l1,3))