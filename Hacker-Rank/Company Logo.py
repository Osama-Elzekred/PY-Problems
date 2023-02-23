
def solve(s):
    d = {}
    l = []
    temp = 0
    for i in s:
        d[i] = d.get(i, 0) + 1
    topvalue = sorted(d, key=d.get, reverse=True)
    # top = sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=False)  # sort by value and then key
    top1, top2, top3 = d[topvalue[0]], d[topvalue[1]], d[topvalue[2]]
    # print(*top[:3], sep="\n")
    # print(topvalue)
    top = [top1, top2, top3]

    for k, v in sorted(d.items()):
        if v in (top1, top2, top3):
            l.append((k, v))
            temp += 1
        if temp == 3:
            break
    temp = 0
    w = 0
    while temp != 3:

        if l[w][1] == top[temp]:
            print(l[w][0], l[w][1])
            l.pop(w)
            temp += 1
            w = 0
        else:
            w += 1


if __name__ == '__main__':
    s = input()
    solve(s)
