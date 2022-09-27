def check(last, domino):
    for i in range(2):
        if domino[i] == last:
            return [True, domino[i-1]]
    return [False, None]


def cin(n):
    # function that woks equally to doing cin >> n
    try:
        n[0] = int(input())
        if n[0] == 0:
            return False
        return True
    except:
        return False


def solve(n, m,  x2, y1,  p):

    used = [0 for i in range(m)]

    def rec(used, last, total_m):

        if total_m == n:
            return x2 == last
        if total_m > n:
            return 0

        found = 0
        # for domino in nums:
        for i in range(len(p)):
            if used[i]:
                continue
            used[i] = 1
            cheeck, newlast = check(last, p[i])
            if cheeck:
                found = rec(used,
                            newlast, total_m+1)
            if found:
                break

            used[i] = False
        return found
        # return False

    return rec(used, y1, 0)


n = [0]
while(cin(n)):
    m = int(input())
    x1, y1 = [int(i) for i in input().split()]
    x2, y2 = [int(i) for i in input().split()]
    p = [list(map(int, input().split())) for a in range(m)]
    print("YES") if solve(n[0], m, x2, y1, p) else print("NO")


# 3
# 4
# 0 1
# 3 4
# 2 1
# 5 6
# 2 2
# 3 2
