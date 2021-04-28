# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.44%)
# Likes:    5590
# Dislikes: 841
# Total Accepted:    527.3K
# Total Submissions: 1.9M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where:
#
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
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
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
#
#
#

#
#

# @lc tags=string;dynamic-programming;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 正则表达式匹配。
# 通配符只有 . * ，这种依赖于之前状态的可以使用动态规划或递归法，这个需要所有的基本结构的解，所以使用动态规划。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 加前置同样字符，是为了计算是否匹配空字符串时，不会出现根本没有计算的情况
        s = ' ' + s
        p = ' ' + p
        # 额外的一个长度，存储初始状态
        r = len(p) + 1
        c = len(s) + 1
        dp = [[False for j in range(c)] for i in range(r)]
        dp[0][0] = True
        for i in range(1, r):
            # 匹配任意字符
            if p[i - 1] == '.':
                for j in range(1, c):
                    dp[i][j] = dp[i - 1][j - 1]
            # 匹配前驱任意个字符
            elif p[i - 1] == '*':
                if p[i - 2] == '.':
                    for j in range(1, c):
                        #           .没有匹配      .多匹配一个    .只匹配一次
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1] or dp[i -
                                                                      1][j - 1]
                else:
                    for j in range(1, c):
                        dp[i][j] = dp[i-2][j] or \
                            ((dp[i][j-1] or dp[i-1][j-1])
                             if p[i-2] == s[j - 1] else False)
            # 匹配特定字符
            else:
                for j in range(1, c):
                    if p[i - 1] == s[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[r - 1][c - 1]

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
    print('s = "aa", p = "a*"')
    print('Output :')
    print(str(Solution().isMatch("aa", "a*")))
    print('Exception :')
    print('true')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "ab", p = ".*"')
    print('Output :')
    print(str(Solution().isMatch("ab", ".*")))
    print('Exception :')
    print('true')
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "aab", p = "c*a*b"')
    print('Output :')
    print(str(Solution().isMatch("aab", "c*a*b")))
    print('Exception :')
    print('true')
    print()

    print('Example 5:')
    print('Input : ')
    print('s = "mississippi", p = "mis*is*p*."')
    print('Output :')
    print(str(Solution().isMatch("mississippi", "mis*is*p*.")))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end