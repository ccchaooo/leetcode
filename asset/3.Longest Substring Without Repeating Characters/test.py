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
      indexforlastmeet = -1
      countwhenmeet = -1
      preindexforblank = -1
      countforblank = 0
      # 头部最长标记,第一次重复时,更新此数据:
      strathead = -1

      if len(s) == 1:
          return 1

      for index, ch in enumerate(list(s)):

        # 处理空字符
        if ch == " " and countforblank == 1:
          countwhenmeet = index - preindexforblank
        else:
          preindexforblank = index
          countforblank = 1

        # 其它字符的处理
        if ch in tempdict :
          if strathead < 0 :
              strathead = tempdict.get(ch) + 1
  
          indexforlastmeet = index
          countwhenmeet = index - tempdict.get(ch)
          if countwhenmeet > total:
            total = countwhenmeet

        tempdict[ch] = index

      # 计算取值
      if countwhenmeet < 0:
        total = len(tempdict)
      elif total < countwhenmeet:
        total = countwhenmeet

      # 头部最长
      if strathead > 0 and total < strathead:
          total = strathead

      # 末端最长的情况
      if indexforlastmeet > 0 and len(s) - indexforlastmeet - 1 > total:
          total = len(s) - indexforlastmeet - 1

      return total

s = 'abba'
so = Solution()
print(so.lengthOfLongestSubstring(s))

