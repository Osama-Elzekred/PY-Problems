import sys


def solve(n, t, tracks):
    nums = [[]]
    mx = [0]

    def rec(idx, sm, collection):

        if idx >= t or sm > n:
            return
        if sm+tracks[idx] <= n and sm+tracks[idx] > mx[0]:
            mx[0] = sm+tracks[idx]
            nums[0] = collection+[tracks[idx]]

        rec(idx+1, sm+tracks[idx], collection+[tracks[idx]])

        rec(idx+1, sm, collection)
    rec(0, 0, [])
    return [mx[0], nums[0]]


for line in sys.stdin:
    tracks = list(map(int, line.split()))
    N = tracks[0]
    t = tracks[1]
    tracks = tracks[2:]
    solution = solve(N, t, tracks)

    for item in solution[1]:
        print(f"{item} ", end="")
    print("sum:" + str(solution[0]))


# 5 3 1 3 4
# 10 4 9 8 4 2
# 20 4 10 5 7 4
# 90 8 10 23 1 2 3 4 5 7
# 45 8 4 10 44 43 12 9 8 2
