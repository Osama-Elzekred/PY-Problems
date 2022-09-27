

import math

#  2 3 5 7 11 13


def solve():
    mx = 1000000
    # n = int(input())
    f_arr = [0 for i in range(mx)]
    # sum_arr=[]
    pairs = []
    for i in range(1, mx+1):
        f_arr[i-1] = is_prime(i-1)
    # print(f_arr)
    for i in range(len(f_arr)-2):
        if f_arr[i] and f_arr[i+2]:
            pairs.append((i, i+2))

    n = int(input())
    print(pairs)
    # sum_arr[0]=f_arr[0]
    # for i in range(1, mx+1):
    #     f_arr[i] += f_arr[i-1]
    # print(f_arr)
    # for i in range(n):
    #     x, y = [int(x) for x in input().split()]
    #     print(f_arr[y]-f_arr[x])


def is_prime(n):
    if n == 2:
        return 1
    if n < 2 or (not n & 1):
        return 0
    for i in range(3, math.floor(math.sqrt(n))+1, 2):
        if n % i == 0:
            return 0

    return 1


solve()
# print(is_prime(9), is_prime(15))
