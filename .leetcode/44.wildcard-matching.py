#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (25.52%)
# Likes:    2865
# Dislikes: 139
# Total Accepted:    297.2K
# Total Submissions: 1.2M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
#
#
# Example 4:
#
#
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
#
#
# Example 5:
#
#
# Input: s = "acdcb", p = "a*c?b"
# Output: false
#
#
#
# Constraints:
#
#
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
#
#
#
#
#
# @lc idea=start
#
# 通配符匹配，‘？’是匹配单个字符，‘*’ 任意多个字符。其实要比 10 题还要简单。因为没有通配符组合的情况了。
# 动态规划，注意交换dp时，需要把首位的True 去掉。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 加前置同样字符，是为了计算是否匹配空字符串时，不会出现根本没有计算的情况
        s = ' ' + s
        p = ' ' + p
        # 额外的一个长度，存储初始状态
        r = len(p)+1
        c = len(s)+1
        dp = [[False for j in range(c)] for i in range(2)]
        dp[1][0] = True
        for i in range(1, r):
            dp[0], dp[1] = dp[1], dp[0]
            dp[1][0] = False
            # 匹配任意字符
            if p[i-1] == '?':
                for j in range(1, c):
                    dp[1][j] = dp[0][j-1]
            # 匹配任意个字符
            elif p[i-1] == '*':
                for j in range(1, c):
                    #          没有匹配    匹配一个  多匹配一个
                    dp[1][j] = dp[0][j] or dp[0][j-1] or dp[1][j-1] 

            # 匹配特定字符
            else:
                for j in range(1, c):
                    if p[i-1] == s[j - 1]:
                        dp[1][j] = dp[0][j-1]
                    else:
                        dp[1][j] = False
        return dp[1][c-1]
# @lc code=end


if __name__ == '__main__':
    # print(Solution().isMatch("aa",  "a"))
    # print(Solution().isMatch("aa",  "*"))
    # print(Solution().isMatch("cb",  "?a"))
    # print(Solution().isMatch("adceb",  "*a*b"))
    # print(Solution().isMatch("acdcb",  "a*c?b"))
    # print(Solution().isMatch("aab",  "c*a*b"))
    print(Solution().isMatch("mississippi",  "m??*ss*?i*pi"))
