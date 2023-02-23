def sieve(limit):
    isComposite = [1 for _ in range(limit+1)]
    isComposite[0] = isComposite[1] = 0
    i = 2
    while i*i <= limit:
        if isComposite[i]:
            for j in range(i*i, limit+1, i):  # start : i*i ,step: j+=i
                isComposite[j] = 0

        i += 1
    primes = set(i for i in range(limit+1) if isComposite[i])
    return primes


def solve():
    t = int(input())
    primes = sieve(2002)
    for i in range(t):
        d = {}
        st = input()
        output = []
        for cr in st:
            d[cr] = d.get(cr, 0)+1
        # print(list(primes))
        for item, count in d.items():
            if count in primes:
                output.append(item)
        if output:
            print(f"Case {i+1}: "+"".join(sorted(output)))
        else:
            print(f"Case {i+1}: "+"empty")


solve()
