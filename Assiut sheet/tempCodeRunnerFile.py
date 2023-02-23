def solve():
#     a, b, q = list(map(int, input().split()))
#     d = {}
#     d[1] = a
#     d[2] = b

#     def rep(q):
#         if d.get(q, False) or q == 0:
#             return d[q]
#         d[q] = rep(q-1) ^ rep(q-2)
#         return d[q]

#     return rep(1) if q == 1 else rep(2) if q == 2 else rep(q)
