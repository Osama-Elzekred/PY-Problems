

import time
start_time = time.time()



def binary_search(l,num2):
      low=0
      high=len(l)-1
     
      while low<=high :
          mid=(low+high)//2
          guess=l[mid]
          if guess==num2 :
              return mid
          elif  guess>num2:
              high=mid-1
          elif guess<num2:
              low=mid+1
      return None


def main():
  set=[]
  n,k=[int(z) for z in input().split()]
  l=[int(num) for num in input().split()]
  for i in range(n):
  #   target=k-l[i]
  #   if target in set:
  #     return print('YES')       
  #   else:
  #     set.append(l[i])
  # return print('NO')
      target=l[i]
      l[i]=-6666
      res=binary_search(sorted(l),k-target)
      if res is not None :
       return print('YES')
  return print('NO')


main()
print("Execution time : " + str((time.time() - start_time)))


 