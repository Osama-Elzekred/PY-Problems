from itertools import product


def sum1(x):
    total = 0
    for i in x:
        total += i**2
    return total


k, m = map(int, input().split())
l = []
for i in range(k):
    l.append(list(map(int, input().split()))[1:])

possible_compinations = product(*l)
results = list(map(lambda x: sum1(x) % m, possible_compinations))
print(max(results))
