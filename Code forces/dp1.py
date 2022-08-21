
def solve(l):
    ans = [[-1]*3]*3
    path = 0

    def dp(row, col, path):
        if row == 0 and col == 0:
            return l[0][0]
        if ans[row][col] != -1:
            return ans[row][col]
        path1, path2 = float("inf"), float("inf")
        if row > 0:
            path1 = dp(row-1, col)
        if col > 0:
            path2 = dp(row, col-1)
        path += min(path1, path2)
        # ans[row][col] =
        return ans[row][col]
    print(dp(2, 2))


l = []
for i in range(3):
    l.append(list(map(int, input().split())))

solve(l)
