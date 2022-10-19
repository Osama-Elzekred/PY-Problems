def sieve(limit):
    isComposite = [1 for _ in range(limit+1)]
    isComposite[0] = isComposite[1] = 0
    i = 2
    while i*i <= limit:
        if isComposite[i]:
            for j in range(i*i, limit+1, i):  # start : i*i ,step: j+=i
                isComposite[j] = 0

        i += 1

    primesList = [i for i in range(limit+1) if isComposite[i]]
    primesSet = set(primesList)
    return (primesList, primesSet)


def solve():

    primeslist, primeSet = sieve(1001)
    ln = len(primeSet)
    sol_f = [0 for i in range(1001)]
    i = 0
    while i < (ln-1):
        test = primeslist[i]+primeslist[i+1]+1
        if test in primeSet and test <= 1000:
            sol_f[test] = 1
        i += 1
    v = 0
    cumsum = [v := v + n for n in sol_f]
    # input
    limit, k = list(map(int, input().split()))
    print("YES") if cumsum[limit] >= k else print("NO")


solve()
