n = int(input())
guess = ["AB", "BB"]
for i in range(n):

    st = list(input())
    l = []
    for i, n in enumerate(st):
        if not l:
            l.append(n)
        else:
            if n == 'A':
                l.append(n)
            else:
                l.pop()
    print(len(l))

    # l, r = 0, 1
    # while l >= 0 and r < len(st):
    #     if st[l]+st[r] in guess:

    #         del st[r]
    #         del st[l]
    #         r = l if l-1 >= 0 else r
    #         l = l-1 if l-1 >= 0 else l
    #     else:
    #         l = r
    #         r += 1

    # print(len(''.join(st)))
