#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.63%)
# Likes:    10277
# Dislikes: 670
# Total Accepted:    1.3M
# Total Submissions: 4.1M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
#
#
# @lc idea=start
#
# 求最长回文子字符串。很朴素的想法，直接遍历，判断是否是回文就可以了。唯一需要注意的就是，回文中心可以是同一个索引，也可以是相邻的两个索引。
#
# @lc idea=end

from typing import *


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.maxS = ''
        for i in range(len(self.s)):
            self. longestPalindromeIndex(i, i)
            self. longestPalindromeIndex(i, i+1)
        return self.maxS

    def longestPalindromeIndex(self, l: int, r: int):
        while(l >= 0 and r < len(self.s) and self.s[l] == self.s[r]):
            l -= 1
            r += 1
        s = self.s[l+1:r]
        if len(s) > len(self.maxS):
            self.maxS = s

# @lc code=end

