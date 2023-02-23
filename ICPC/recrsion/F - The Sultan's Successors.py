
def solve():
    board = [list(map(int, input().split())) for i in range(8)]
    valid = [[0 for i in range(8)] for j in range(8)]
    sums = [-1]

    def vaalid(valid, r, c):
        return valid[r][c]
        # for i in range(8):
        #     for j in range(8):
        #         if r == i and not valid[i][j]:
        #             return False
        #         if j == c and not valid[i][j]:
        #             return False
        #         if (j-i) == (c-r) and not valid[i][j]:
        #             return False
        #         if (i+j) == (c+r) and not valid[i][j]:
        #             return False
        # return True
        # 1 1 1 1 1 1 1 1   0 3
        # 1 1 1 1 1 1 1 1   1 2
        # 1 1 1 1 1 1 1 1   2 1
        # 1 1 1 1 1 1 1 1
        # 1 1 1 1 1 1 1 1

    def set_valid(valid, r, c, val):
        for i in range(8):
            for j in range(8):
                if r == i:
                    valid[i][j] += val
                if j == c:
                    valid[i][j] += val
                if (j-i) == (c-r):
                    valid[i][j] += val
                if (i+j) == (c+r):
                    valid[i][j] += val

    def rec(r, c, valid, sm):
        if c == 8:
            r, c = r+1, 0
        if r >= 8:
            return 0

        if r == 7 or c == 7 and vaalid(valid, r, c):
            sm += board[r][c]
            sums[0] = max(sums[0], sm)

        if vaalid(valid, r, c):

            set_valid(valid, r, c, -1)
            rec(r, c+1, valid,  sm+board[r][c])
            set_valid(valid, r, c, 1)

        rec(r, c+1, valid, sm)

    rec(0, 0, valid, 0)
    return sums[0]


t = int(input())
for i in range(t):
    print(solve())
