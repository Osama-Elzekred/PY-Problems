from itertools import product
# temp2 = (5+(pow(2, 2)))
# print(temp2)
l = [[3, 45], [6, 7]]
# temp = max(l)
# print(temp)
possible_compinations = product(*l)
print(list(possible_compinations))
