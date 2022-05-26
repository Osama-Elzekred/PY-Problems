# Taking multiple values 
x = list(map(int, input("Enter multiple values: ").split()))
x = [int(x) for x in input().split()]
print(x)


# time
import time
start_time = time.time()
# *** YOUR CODE ***
print("Execution time : " + str((time.time() - start_time)))