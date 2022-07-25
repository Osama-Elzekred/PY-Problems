def searchRange(nums, target):
    l, r = 0, len(nums)-1
    index = (l+r)//2
    output = [-1, -1]
    if not nums:
        return output
    while l <= r:
        index = (l+r)//2
        mid = nums[index]
        if mid == target:
            while nums[l] != mid:
                l += 1
            while nums[r] != mid:
                r -= 1
            output = [l, r]
            break
        elif mid < target:
            l = index+1
        elif mid > target:
            r = index-1

    return output


print(searchRange([0, 0, 1, 1, 1, 2, 2, 3, 3, 3,
      4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10], 4))
