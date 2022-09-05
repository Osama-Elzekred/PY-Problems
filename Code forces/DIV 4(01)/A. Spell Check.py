

# import sys


def solve():
    n = int(input())

    for i in range(n):
        m = int(input())
        s = {'T', 'i', 'm', 'u', 'r'}
        s2 = set()
        flag = 0
        st = input()
        if m != 5:
            print("No")
            continue
        for let in st:
            if let not in s or let in s2:
                print("No")
                flag = 1
                break
            s2.add(let)
        if not flag:
            print("Yes")


solve()
