def solve():

    def rec(r, c):
        if r >= n or r < 0 or c >= m or c < 0:
            return 0
        if maze[r][c] == '#' or vis[r][c]:
            return 0
        if (r != r0 or c != c0) and (r == 0 or c == 0 or r == n-1 or c == m-1):
            return 1
        vis[r][c] = 1
        found = 0
        found = rec(r+1, c)
        if not found:
            found = rec(r-1, c)
        if not found:
            found = rec(r, c+1)
        if not found:
            found = rec(r, c-1)
        if found:
            return 1

    n, m = [int(x) for x in input().split()]
    maze = []
    for i in range(n):
        maze.append(input())
    vis = [[0]*m for j in range(n)]
    pathes = set()
    # col 0
    for r in range(n):
        if maze[r][0] == '.':
            pathes.add((r, 0))
    # col m
    for c in range(n):
        if maze[c][m-1] == '.':
            pathes.add((c, m-1))
    # row 0
    for r in range(m):
        if maze[0][r] == '.':
            pathes.add((0, r))
    # row n
    for c in range(m):
        if maze[n-1][c] == '.':
            pathes.add((n-1, c))

    if len(pathes) != 2:
        return 0

    pathes = list(pathes)
    # r,c
    r0, c0 = pathes[0][0], pathes[0][1]

    return rec(r0, c0)


t = int(input())
for i in range(t):
    print("valid") if solve() else print("invalid")
