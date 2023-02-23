def solve():
    n, x = [int(i) for i in input().split()]
    nums = []
    for i in range(n):
        nums.append([int(i) for i in input().split()][1:])

    def rec(pro, index):
        if pro == x and index == n:
            return 1
        if index == n or pro > x:
            return 0
        c = 0
        for item in nums[index]:
            c += rec(pro*item, index+1)

        return c

    return rec(1, 0)


print(solve())
