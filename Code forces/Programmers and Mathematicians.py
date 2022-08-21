def solve():
    def check(num_of_teams):
        if a > b:
            mx, mn = a, b
        else:
            mx, mn = b, a
        counter = 0

        while mx > 1:
            if mx >= 3 and mn > 0:
                mx -= 3
                mn -= 1
                counter += 1
            elif mx == 2 and mn == 2:
                mx -= 2
                mn -= 2
                counter += 1
            else:
                break

            if mx > mn:
                mx, mn = mx, mn
            else:
                mx, mn = mn, mx

        return counter >= num_of_teams

    n = int(input())
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        l, r = 0, (a+b)//4
        ans = -1
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        print(ans)


for s in [*open(0)][1:]:
    a, b = map(int, s.split())
    print(min(a, b, (a+b) // 4))

# solve()
for s in [*open(0)][1:]:
    a, b = map(int, s.split())
    print(min(a, b, a+b >> 2))
