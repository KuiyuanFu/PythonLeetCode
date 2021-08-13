# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (49.80%)
# Likes:    2926
# Dislikes: 251
# Total Accepted:    327.8K
# Total Submissions: 658.1K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
# >= 10^9, and you want to check one by one to see if t has its subsequence. In
# this scenario, how would you change your code?
#

# @lc tags=binary-search;dynamic-programming;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个字符串是否是另一个的子序列。
# 对s中的字符依次在t中寻找。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, len(t)
        for c in s:
            while l < r:
                if t[l] == c:
                    break
                l += 1

            if l == r:
                return False
            l += 1
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abc", t = "ahbgdc"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSubsequence("abc", "ahbgdc")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "axc", t = "ahbgdc"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSubsequence("axc", "ahbgdc")))
    print()

    pass
# @lc main=end