
def maxXor(lo, hi, k):

    l = []
    mx = 0

    for i in range(lo, hi):
        for j in range(lo+1, hi):
            a = i ^ j
            if a <= k:
                mx = max(mx, a)
    return mx


print(maxXor(1, 8, 6))
