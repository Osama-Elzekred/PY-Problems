

def d(n: int):
    if n == 1:
        return 0
    sm = 1
    i = 2
    while i*i <= n:
        if n/i == i:
            sm += i
            break
        if n % i == 0:
            sm += i
            sm += n//i
        i += 1
    return sm


def solve():
    n = int(input())
    for i in range(n):
        print(d(int(input())))


solve()
