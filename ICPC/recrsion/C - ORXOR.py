def solve():
    n = int(input())
    l = [int(x) for x in input().split()]
    ans = float("inf")
    for i in range(1 << n):
        tempOR, tempXOR = 0, 0
        for j in range(n):
            tempOR |= l[j]
            if (i & (1 << j)):
                tempXOR ^= tempOR
                tempOR = 0
        tempXOR ^= tempOR
        ans = min(ans, tempXOR)
    return ans


print(solve())
