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
            low, high = mid-1, mid+1
            while nums[low] == mid:
                low -= 1
            while nums[high] == mid:
                high += 1
            output = [low, high]
            break
        elif mid < target:
            l = index+1
        elif mid > target:
            r = index-1

    return output


print(searchRange([0, 0, 1, 1, 1, 2, 2, 3, 3, 3,
      4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10], 4))
