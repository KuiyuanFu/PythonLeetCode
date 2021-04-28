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

# @lc tags=string;dynamic-programming;backtracking;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 通配符匹配，‘？’是匹配单个字符，‘*’ 任意多个字符。
# 其实要比 10 题还要简单。因为没有通配符组合的情况了。
# 动态规划，注意交换dp时，需要把首位的True 去掉。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=4


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 加前置同样字符，是为了计算是否匹配空字符串时，不会出现根本没有计算的情况
        s = ' ' + s
        p = ' ' + p
        # 额外的一个长度，存储初始状态
        r = len(p) + 1
        c = len(s) + 1
        dp = [[False for j in range(c)] for i in range(2)]
        dp[1][0] = True
        for i in range(1, r):
            dp[0], dp[1] = dp[1], dp[0]
            dp[1][0] = False
            # 匹配任意字符
            if p[i - 1] == '?':
                for j in range(1, c):
                    dp[1][j] = dp[0][j - 1]
            # 匹配任意个字符
            elif p[i - 1] == '*':
                for j in range(1, c):
                    #          没有匹配    匹配一个  多匹配一个
                    dp[1][j] = dp[0][j] or dp[0][j - 1] or dp[1][j - 1]

            # 匹配特定字符
            else:
                for j in range(1, c):
                    if p[i - 1] == s[j - 1]:
                        dp[1][j] = dp[0][j - 1]
                    else:
                        dp[1][j] = False
        return dp[1][c - 1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aa", p = "a"')
    print('Output :')
    print(str(Solution().isMatch("aa", "a")))
    print('Exception :')
    print('false')
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aa", p = "*"')
    print('Output :')
    print(str(Solution().isMatch("aa", "*")))
    print('Exception :')
    print('true')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "cb", p = "?a"')
    print('Output :')
    print(str(Solution().isMatch("cb", "?a")))
    print('Exception :')
    print('false')
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "adceb", p = "*a*b"')
    print('Output :')
    print(str(Solution().isMatch("adceb", "*a*b")))
    print('Exception :')
    print('true')
    print()

    print('Example 5:')
    print('Input : ')
    print('s = "acdcb", p = "a*c?b"')
    print('Output :')
    print(str(Solution().isMatch("acdcb", "a*c?b")))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end