s={1,2,3,4,4,9,7,5,6,7,8}
s.add(11)
s.remove(23)
s.discard(23)
s.update(set([-15,65,-32]))
for i in s :
  print(i)


# list1 = [1, 2, 3, 4]
# list2 = [10, 41, 3, 4, 5]
# alphabet_set = {'a', 'b', 'c'}
 
# # lists converted to sets
# set1 = set(list2)
# set2 = set(list1)
 
# # Update method
# # set1.update(set2)
 
# # Print the updated set
# print(set2)

# set2.difference_update(set1)
# print(set2)
# set1.update(alphabet_set)
# print(set1)
# t=tuple("sdfa")
# t.__iter__();
# t_iter=iter(t)
# print(t[-1])
# z=t.index('s')
# print(z)
# x=enumerate(t)
# for x,y in x :
#   print(x,y)
#  result = "0.00+%.2fi" % (self.imaginary)  for float displaying , import math 
# res=[1,5,6,4,7]
# print(*res,*(4,5,36,5))
# print(*map(lambda x: x**2,res))
# d={3:1, 1:2, 2:3, 4:4}
# print(*d)
# print(**d)
print(*zip([1,2,3],range(3)))
from itertools import permutations