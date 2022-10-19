def primeFactorscount(n):
    s = set()
    i = 2
    while i*i <= n:
        if n % i == 0:
            s.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        s.add(n)
    return len(s)


def cin(n):
    try:
        n[0] = int(input())
        return n[0]
    except:
        return False


n = [0]
while cin(n):
    print(f"{n[0]} : {primeFactorscount(n[0])}")
