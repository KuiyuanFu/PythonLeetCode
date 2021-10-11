# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#
# https://leetcode.com/problems/strange-printer/description/
#
# algorithms
# Hard (42.81%)
# Likes:    668
# Dislikes: 59
# Total Accepted:    20.1K
# Total Submissions: 46.7K
# Testcase Example:  '"aaabbb"'
#
# There is a strange printer with the following two special properties:
#
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending
# at any place and will cover the original existing characters.
#
#
# Given a string s, return the minimum number of turns the printer needed to
# print it.
#
#
# Example 1:
#
#
# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#
#
# Example 2:
#
#
# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of
# the string, which will cover the existing character 'a'.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s consists of lowercase English letters.
#
#
#

# @lc tags=dynamic-programming;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 打印机，每次打印一种字符，字符可以被覆盖。求最少的打印次数。
# 动态规划。
# 边界的字符必须消耗一次打印次数，并额外可能将内部的同种类字符打印出来。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        ss = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ss.append(s[i])
        length = len(ss)
        dp = [[1 for _ in range(length)] for _ in range(length)]
        for step in range(1, length):
            for l in range(0, length - step):
                r = l + step
                res = 1 + min(dp[l][r - 1], dp[l + 1][r])
                for m in range(l, r):
                    if ss[m] == ss[r]:
                        res = min(res, dp[l][m] + dp[m + 1][r] - 1)
                dp[l][r] = res
        return dp[0][-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aaabbb"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().strangePrinter("aaabbb")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aba"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().strangePrinter("aba")))
    print()
    print('Exception :')
    print('3')
    print(str(Solution().strangePrinter("ababa")))
    print('Exception :')
    print('19')
    print(
        str(Solution().strangePrinter(
            "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa")))
    pass
# @lc main=end