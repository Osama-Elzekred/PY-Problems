from cmath import sqrt
from functools import reduce


# print(float("infinity") > 1)
# print(len([None]*5))
t = reduce(lambda acc, x: acc+sqrt(x), [1, 4, 9, 16])
print(t)
