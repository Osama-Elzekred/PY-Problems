

def solve():
  matrix = []
  n=int(input())  
  
  for i in range(n):          
      a =[] 
      a= list(map(int, input().split()))
      matrix.append(a)
  temp=n
  # print(matrix)
  for i in range(n): 
    if matrix[i][i]!=temp: 
      return"NO"
  for i in range(n): 
    for j in range(n): 
      if i==j: continue
      if matrix[i][j]!=0:
        return "NO"
  return "YES" 



print(solve())
