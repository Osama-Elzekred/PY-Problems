
import time
start_time = time.time()



def main():
  t=int(input())
  sum=0
  temp=0
  while t>0:
    n,b,x,y=[int(x) for x in input().split()]
    sum=0
    temp=0
    for _ in range(n):
      if sum+x>b:
        sum-=y
        temp+=sum
      else :
         sum+=x 
         temp+=sum
        #  print(sum)
    print(temp)
    t-=1

main()
print("Execution time : " + str((time.time() - start_time)))

# 5 100 1 30