t = int(input())
for i in range(t):
    n = int(input())
    j = 0
    while True:
        if j & n > 0 and j ^ n > 0:
            print(j)
            break
        j += 1
