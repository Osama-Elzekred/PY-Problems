class Solution(object):
    def searchInsert(self, nums, target):

        if target <= nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            guess = nums[mid]
            if(guess == target):
                return mid
            if(guess > target):
                high = mid-1
            else:
                low = mid+1
        return low+1


l = list(map(int, input().split()))
target = int(input())


s = Solution()
print(s.searchInsert(l, target))
