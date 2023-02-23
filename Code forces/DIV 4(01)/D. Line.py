

def solve():
    for _ in range(int(input())):
        n = int(input())
        st = st = list(map(str, input()))
        sm = 0
        for i in range(n):
            if (st[i] == 'L'):
                sm += i
            else:
                sm += (n-i-1)
        p1, p2 = 0, n-1
        y = n
        while y and p1 < (n//2):
            if st[p1] == 'L':
                sm -= p1
                sm += (n-p1-1)
                print(sm, end=' ')
                y -= 1

            if st[p2] == 'R':

                sm -= (n-p2-1)
                sm += p2
                print(sm, end=' ')
                y -= 1

            p1 += 1
            p2 -= 1

        for i in range(y):
            print(sm, end=' ')

        print()


solve()
