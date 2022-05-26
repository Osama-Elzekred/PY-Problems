from collections import Counter, OrderedDict
Dict = {}
for x in sorted(input()):
    Dict[x] = Dict.get(x, 0)+1
# Sorting Dict by value & storing sorted keys in Dict_keys.
print(Dict)
# sort by value but return list of keys of those values
Dict_keys = sorted(Dict, key=Dict.get, reverse=True)

print(Dict_keys)
for key in Dict_keys[:3]:
    print(key, Dict[key])


# class OrderedCounter(Counter, OrderedDict):
#     pass
# qwertyuiopasdfghjklzxcvbnm
# aabbbccde

[print(*c) for c in Counter(sorted(input())).most_common(3)]
