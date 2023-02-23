t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    flag = False
    m = 0
    for j in range(n):
        if b[j] != 0:
            m = a[j]-b[j]
            break
    for k in range(n):
        if (b[k] > a[k]) or ((a[k]-b[k]) != m):
            print("NO")
            flag = True
            break
        # if (b[k] == 0 and (a[k]-b[k]) >= m):
        #     print("NO")
        #     flag = True
        #     break

    if not flag:
        print("YES")


# YES
# YES
# NO
# NO
# YES
# NO
