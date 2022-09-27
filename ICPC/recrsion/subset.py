
def solve():
    # n = int(input())
    # l = [int(x) for x in input().split()]
    l = input()
    n = len(l)
    maxsub = ""
    for i in range(1 << n):
        mask, y = i, 0
        st = ""
        while mask:
            if mask & 1:
                st += l[y]
            y += 1
            mask = mask >> 1
        maxsub = max(st, maxsub)
        # print(st)
    print(maxsub)


solve()
