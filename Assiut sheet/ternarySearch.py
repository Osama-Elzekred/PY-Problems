import math


def solve():
    n = int(input())
    fr = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        fr.append((x, y))
    fr = sorted(fr, key=lambda x: x[0])

    def f(x):
        res = 0
        for x1, y1 in fr:
            res = max(res, math.hypot((x-x1), (y1)))
        return res

    l, r = fr[0][0], fr[-1][0]
    while r-l > 0.0000001:
        m1, m2 = l+(r-l)/3, r-(r-l)/3
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return (l+r)/2


print('%.5f' % solve())
