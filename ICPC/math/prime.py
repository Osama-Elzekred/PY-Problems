import math


def solve():
    mx = 1000000
    f_arr = [0 for i in range(mx)]
    pairs = []
    for i in range(1, mx+1):
        f_arr[i-1] = is_prime(i-1)

    for i in range(len(f_arr)-2):
        if f_arr[i] and f_arr[i+2]:
            pairs.append((i, i+2))
    n = int(input())
    print(pairs)


def is_prime(n):
    if n == 2:
        return 1
    if n < 2 or (not n & 1):
        return 0
    for i in range(3, math.floor(n**0.5)+1, 2):
        if n % i == 0:
            return 0

    return 1


def sieve(limit):
    isComposite = [1 for _ in range(limit+1)]
    isComposite[0] = isComposite[1] = 0
    i = 2
    while i*i <= limit:
        if isComposite[i]:
            for j in range(i*i, limit+1, i):  # start : i*i ,step: j+=i
                isComposite[j] = 0

        i += 1
    primes = [i for i in range(limit+1) if isComposite[i]]
    return primes


def primeFactors(n):
    i = 2
    primesfactors = []
    while i*i <= n:
        if n % i == 0:
            primesfactors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        primesfactors.append(n)
    return primesfactors


# print(sieve(100))
print(primeFactors(int(input())))
# solve()
# print(is_prime(9), is_prime(15))
