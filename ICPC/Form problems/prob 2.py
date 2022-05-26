

def main ():
  n=int(input())
  sums=[]
  
  while n>0:
    nums=[int(x) for x in input().split()]
     # take multiple input in one line and put it in list
    sums.append(sumfun(nums))
    n=n-1
  for item in sums :
      print(item)

def sumfun(l):
 sum1=0
 for item in l :
  sum1+=item
 return sum1

main()