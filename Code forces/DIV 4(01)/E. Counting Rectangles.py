

def solve():
    for _ in range(int(input())):
        grid = arr = [[0 for i in range(1001)] for j in range(1001)]
        # print(grid)
        n, q = list(map(int, input().split()))
        for _ in range(n):
            h, w = list(map(int, input().split()))
            grid[h][w] += h*w
        # print(grid)
        for i in range(1, 1000):
            for j in range(1, 1000):
                grid[i][j] += grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
        # print(grid)
        for _ in range(q):
            h1, w1, h2, w2 = list(map(int, input().split()))
            print(grid[h2-1][w2-1]-grid[h2-1][w1]-grid[h1][w2-1]+grid[h1][w1])


# sys.stdin = open("input.txt", 'r')
solve()
