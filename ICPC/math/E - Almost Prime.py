def primeFactors(n):
    i = 2
    primesfactors = set()
    while i*i <= n:
        if n % i == 0:
            primesfactors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        primesfactors.add(n)
    return 1 if len(primesfactors) == 2 else 0


sm = 0
for i in range(1, int(input())+1):
    sm += primeFactors(i)
print(sm)


# print(primeFactors(19))
