from sys import stdin


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
    print(*primesfactors, sep=' x ')
    # return primesfactors


def print_frist(n):

    print(f"{n} = -1 x ", end='') if n < 0 else print(f"{n} = ", end='')


while t := int(stdin.readline()):
    print_frist(t)
    primeFactors(abs(t))
