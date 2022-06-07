
t = int(input())


for i in range(t):
    n, k = [int(z) for z in input().split()]
    x = k
    s = input()
    for i in range(n):

        if n > i+(k-1):
            st = s[i:i+k]
            # print(st)
            num = st.count('W')
            if num < x:
                x = num
            if x == 0:
                break
    print(x)


# 4
# 5 3
# BBWBW
# 5 5
# BBWBW
# 5 1
# BBWBW
# 1 1
# W


# 1
# 2
# 0
# 1
