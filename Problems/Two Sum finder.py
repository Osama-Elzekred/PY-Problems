class Solution(object):
    
    def binary_search(self,l,num2):
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

    
    def twoSum(self, nums, target):
       p=Solution()
       l=nums.copy()
       x=target
       l.sort()
       for i in range(len(l)) :
         num1=l[i]
         num2=x-num1
         res= p.binary_search(l,num2)
         if res is not None :
           a=nums.index(num1)
           nums[nums.index(num1)]=-6666666
           s=[a,nums.index(num2)]
           s.sort()
           return s 
           
# l=[*range(15)]        
f=Solution()
print(*f.twoSum([3,2,4],6))



# print(enumerate(l))