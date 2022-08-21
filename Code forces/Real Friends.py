def solve():
    (n, k) = list(map(int, input().split()))
    l = list(map(str, input().split()))

    Dict = {}
    for x in sorted((''.join(l))):
        Dict[x] = Dict.get(x, 0)+1

    Dict_keys = sorted(Dict.items(), key=lambda x: (
        x[1], x[0]), reverse=True)[:k]
    if len(Dict.keys()) < k:
        print("I'm not happy")
        return

    for key in Dict_keys:
        print(key[0], end=' ')


solve()
