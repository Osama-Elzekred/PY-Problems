def primeFactors(n):
    d = {}
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            d[i] = d.get(i, 0)+1
        else:
            i += 1
    if n > 1:
        d[n] = d.get(n, 0)+1
    return d


def cin(n):
    try:
        n[0] = int(input())
        return n[0]
    except:
        return False


n = [0]
while cin(n):
    d = primeFactors(n[0])
    for k, v in sorted(d.items()):
        print(f"{k}^{v} ", end="")
    print()
