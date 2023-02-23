def solve():
    (n, m, a, b) = list(map(int, input().split()))
    if (m * a <= b):
        print(n * a)
        return

    res2 = (n//m)*b + min((n % m) * a, b)
    print(res2)


solve()
