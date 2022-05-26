from collections import defaultdict 
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(lambda : 0)
# d["a"] = 1
# d["b"] = 2
  
f=dict()
d['a']=1
d['a'].append(4)
d['b'].append(5)
print(d)
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)
print(d['dsf'])
print(len(d['dsf'])==0)


# Defining the dict
d = defaultdict(int)
   
L = [1, 2, 3, 4, 2, 4, 1, 2]
   
# Iterate through the list
# for keeping the count
for i in L:
       
    # The default value is 0
    # so there is no need to 
    # enter the key first
    d[i] += 1




# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict 

n,m=input().split()
b=[]
d=defaultdict(list)
for i in range(int(n)):
    d[input()].append(i+1)
for i in range(int(m)):
    x=input()   
    print(*d[x]) if len(d[x])>0 else print(-1)
