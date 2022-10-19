import math


def is_prime(n):
    if n == 2 or n == 3:
        return 1
    if n < 2 or (not n & 1):
        return 0
    if n % 3 == 0:
        return 0
    for i in range(5, math.floor(n**0.5)+1, 4):
        if n % (i+2) == 0 or n % i == 0:
            return 0

    return 1


def solve():
    n = int(input())
    for _ in range(n):
        x, y = list(map(int, input().split()))
        for item in range(x, y+1):
            if is_prime(item):
                print(item)
        print()


solve()
