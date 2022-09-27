

def solve():
    l = [int(x) for x in input().split()]
    possible = 0
    for i in range(1 << len(l)):
        a, b = 0, 0
        y = 0
        mask = i
        for _ in range(4):
            if mask & 1:
                a += l[y]
            else:
                b += l[y]
            y += 1
            mask = mask >> 1
        if a == b:
            possible = 1
            print("YES")
            break
    if not possible:
        print("NO")


def recSolve():
    l = [int(x) for x in input().split()]

    def rec(idx, Amask, Bmask):
        if idx == 4:
            return Amask == Bmask

        found = 0
        found = rec(idx+1, Amask + l[idx], Bmask)
        if not found:
            found = rec(idx+1, Amask, Bmask + l[idx])

        return found

    return rec(0, 0, 0)


print("Yes") if recSolve() else print("No")
