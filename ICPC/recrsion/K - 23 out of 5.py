import sys
from itertools import permutations


def solve(nums):
    expressions = ["+", "*", "-"]

    def rec(idx, total):
        if idx == 5:
            return total == 23

        # newnum = nums[idx]

        found = 0
        for exp in expressions:
            if exp == '+' and not found:
                found = rec(idx+1, total+nums[idx])
            if exp == '*' and not found:
                found = rec(idx+1, total*nums[idx])
            if exp == '-' and not found:
                found = rec(idx+1, total-nums[idx])
        return found
        # return rec(idx+1, total+newnum) or rec(idx+1, total-newnum) or rec(idx+1, total*newnum)

    return rec(1, nums[0])


for line in sys.stdin:
    nums = list(map(int, line.split()))
    if all(item == 0 for item in nums):
        break
    nums = sorted(nums)
    possible = 0
    p = permutations(nums)
    for item in list(p):
        possible = solve(item)
        if possible:
            break

    print("Possible") if possible else print("Impossible")
