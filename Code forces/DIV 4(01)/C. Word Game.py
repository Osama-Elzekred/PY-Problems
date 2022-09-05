

def solve():

    for _ in range(int(input())):
        s1, s2, s3 = 0, 0, 0
        n = int(input())
        l = {}
        l1 = {item for item in map(str, input().split(" "))}
        l2 = {item for item in map(str, input().split(" "))}
        l3 = {item for item in map(str, input().split(" "))}
        for item in l1:
            l[item] = l.get(item, 0)+1
        for item in l2:
            l[item] = l.get(item, 0)+1
        for item in l3:
            l[item] = l.get(item, 0)+1

        for word, val in l.items():
            if val == 3:
                continue
            p1 = word in l1
            p2 = word in l2
            p3 = word in l3
            if val == 1:
                if p1:
                    s1 += 3
                if p2:
                    s2 += 3
                if p3:
                    s3 += 3
                continue
            if p1 and p2:
                s1, s2 = s1+1, s2+1
            if p1 and p3:
                s1, s3 = s1+1, s3+1
            if p3 and p2:
                s3, s2 = s3+1, s2+1
        print(s1, s2, s3)

        # for item in l3:
        #     if item in l1 and not item in l2:
        #         p[0], p[2] = p[0]+1, p[2]+1
        #         p[1] += 3
        #     if not item in l1 and item in l2:
        #         p[1], p[2] = p[1]+1, p[2]+1
        #         p[0] += 3
        #     if not item in l1 and not item in l2:
        #         p[0], p[1], p[2] = p[0]+3, p[1]+3, p[2]+3


solve()
