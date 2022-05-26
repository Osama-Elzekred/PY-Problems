


import time
start_time = time.time()
def main():
  n,k=[int(z) for z in input().split()]
  l=[int(num) for num in input().split()]
  for i in range(n):
    target=l[i]
    l[i]=None
    if next((x for x in l if x==k-target), None) != None :
     return print('YES')
  return print('NO')
main()
# *** YOUR CODE ***
print("Execution time : " + str((time.time() - start_time)))