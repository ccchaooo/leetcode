# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        items = [item(k, v) for k, v in enumerate(self.nums)]
        items.sort(key=lambda x: x.v, reverse=False)
        for i, x in enumerate(items):
            j = i + 1
            while j < len(items):
                if x.v + items[j].v == target:
                    ret = [x.k, items[j].k]
                    return ret
                elif x.v + items[j].v > target:
                    break
                j = j + 1
        return 0


class item(object):

    def __init__(self, k, v):
        self.k = k
        self.v = v


li = [3,2,4]
So = Solution()
print(So.twoSum(li,5))