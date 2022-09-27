# def solve(l):
#     mem = {}
#     path = 0

#     def dp(row, col, path):
#         if row == 0 and col == 0:
#             return 1
#         if mem.get((row, col), False):
#             return mem[(row, col)]

#         cur = min(dp(row, col-1, path+1), dp(row-1, col, path+1))
#         # cur = max(cur, dp(pos-1, sm))
#         mem[(row, col)] = cur
#         return cur
#     return dp(len(l))


# def solve(l):
#     mem = {}
#     # path = 0
#     l=[]
#     num=int(input())
#     for i in range(num):
#        n, m = list(map(int, input().split()))
#        l.append((n,m))


#     # n,m=list(map(int, input().split()))
#     grid=[[0 for i in range(n)] for j in range(n)]
#     def rec(r,c,w):
s = "Ahmed"
s = sorted(s)
print("".join(s))


# def solve(l, target):
#     mem = {}
#     def dp(pos, sm):
#         if sm == 0:
#             return 1
#         if pos == 0 or sm < 0:
#             return 0
#         if mem.get((pos, sm), False):
#             return mem[(pos, sm)]
#         cur = 0
#         cur = max(cur, dp(pos-1, sm-l[pos-1]))
#         cur = max(cur, dp(pos-1, sm))
#         mem[(pos, sm)] = cur
#         return cur
#     return dp(len(l), target)
# print(solve([4, 6, 7, 8, 9], 11))
