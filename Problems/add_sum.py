
nums = [*range(0,100)]
targets =28
for i in nums:
  num1=nums[i]
  nums[i]=-6666666666
  num2=targets-num1
  if num2 in nums :
    print([i,nums.index(num2)])
    break
