
n = int(input())
for i in range(n):
    N, M = [int(x) for x in input().split()]
    s = set()
    for j in range(N):
        K, V = [x for x in input().split()]
        s.add((K, V))
    # print(len(s))
    if (len(s) != N):
        print("YES")
    else:
        print("NO")
