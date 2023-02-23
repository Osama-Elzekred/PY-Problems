import re


class Solution(object):

    def twoSum(self, nums, target):
        prevItem = {}
        for i, n in enumerate(nums):
            n2 = target-n
            if n2 in prevItem.keys():
                return[prevItem[n2], i]

            prevItem[n] = i
        return []


print(list(enumerate([1, 23, 6, 5, 4])))
