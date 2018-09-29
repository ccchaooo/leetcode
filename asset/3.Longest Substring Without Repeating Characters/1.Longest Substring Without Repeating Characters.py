# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

class Solution:
    def lengthOfLongestSubstring(self, s):
      tempdict = {}
      total = 0
      count = 0
      countforblank = 0

      if len(s) == 1:
          return 1

      for index, ch in enumerate(list(s)):

        # 处理空字符
        if ch == " " and countforblank == 1:
            total = len(tempdict)
            tempdict = {}
            tempdict[ch] = index
            countforblank = 1

        # 其它字符的处理
        if ch in tempdict:
          if (len(tempdict) > total):
              total = len(tempdict)
          tempdict = {}
          tempdict[ch] = index
          count = 1
        else:
          tempdict[ch] = index
          count = count + 1

      return total if total > count else count

s = 'dvdf'
so = Solution()
print(so.lengthOfLongestSubstring(s))

