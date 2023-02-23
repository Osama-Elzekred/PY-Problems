t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    for item in l:
        if item % 2 == 0:
            count += 1
    print(count)
