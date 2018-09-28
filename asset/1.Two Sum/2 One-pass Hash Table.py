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
        self.dc ={}
        for i, x in enumerate(self.nums):
            if self.target - x in self.dc:
                ret = [self.dc.get(self.target - x), i]
                return ret
            self.dc[x] = i

        return 0


li = [3, 2, 4]
So = Solution()
print(So.twoSum(li, 5))
