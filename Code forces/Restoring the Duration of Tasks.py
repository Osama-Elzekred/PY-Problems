t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    d = []
    d.append(f[0]-s[0])
    for i in range(1, n):
        if s[i]-f[i-1] > 0:
            d.append(f[i]-s[i])
        else:
            d.append(f[i]-f[i-1])

    d = list(map(str, d))
    print(' '.join(d))

# 4
# 3
# 0 3 7
# 2 10 11
# 2
# 10 15
# 11 16
# 9
# 12 16 90 195 1456 1569 3001 5237 19275
# 13 199 200 260 9100 10000 10914 91066 5735533
# 1
# 0
# 1000000000


# 2 7 1
# 1 1
# 1 183 1 60 7644 900 914 80152 5644467
# 1000000000
