# from collections import heapq
import heapq

l = [5, 6, 7, 1, 9]
heapq.heapify(l)
print(l)
heapq.heappush(l, 6)
print(l)
s = heapq.heappop(l)
print(s)
x = heapq.heappushpop(l, 10)
print(x)
print(l)
# print(-float("inf") == float("-inf"))
# d = {None: 1}
# d.update({3: 4})
# d.setdefault(0, 0)
# del d[3]
# def dd(): pass


# print(dd())
# q.insert(5)
# q.insert(1)
# q.insert(7)
# q.insert(9)
# print(q)
