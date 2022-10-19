from sys import stdin, stdout


def gcd(a, b):

    if a == 0:
        return b
    return gcd(b % a, a)


# ma = {}

# Function that calculate the count of
# each prime factor of a number


# def primeFactorize(a):

#     sqt = int(math.sqrt(a))
#     for i in range(2, sqt, 2):
#         cnt = 0

#         while (a % i == 0):
#             cnt += 1
#             a /= i

#         ma[i] = cnt

#     if (a > 1):
#         ma[a] = 1


# def primeFactors(n):
#     i = 2
#     cnt = 0
#     out = 1
#     while i*i <= n:
#         if n % i == 0:
#             cnt += 1
#             n //= i
#         else:
#             out *= (cnt+1)
#             cnt = 0
#             i += 1
#     if n > 1 and n == i and cnt:
#         cnt += 1
#         out *= (cnt+1)
#     elif n > 1 and n != i and cnt:
#         out *= (cnt+1)
#         out *= 2
#     elif cnt:
#         out *= (cnt+1)
#     elif n > 1:
#         out *= 2
#     return out


def d(n: int):
    if n == 1:
        return 0
    sm = 2
    i = 2
    while i*i <= n:
        if n/i == i:
            sm += 1
            break
        if n % i == 0:
            sm += 2
        i += 1
    return sm


for i in range(int(input())):
    x, y = l = [int(x) for x in stdin.readline().split()]
    if x >= y:
        mx, mn = x, y
    else:
        mx, mn = y, x
    gc = gcd(mn, mx)
    stdout.write(str(d(gc))+'\n')
