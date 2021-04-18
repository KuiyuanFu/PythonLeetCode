# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (16.04%)
# Likes:    906
# Dislikes: 5589
# Total Accepted:    200.3K
# Total Submissions: 1.2M
# Testcase Example:  '"0"'
#
# A valid number can be split up into these components (in order):
#
#
# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
#
#
# A decimal number can be split up into these components (in order):
#
#
# (Optional) A sign character (either '+' or '-').
# One of the following formats:
#
# At least one digit, followed by a dot '.'.
# At least one digit, followed by a dot '.', followed by at least one
# digit.
# A dot '.', followed by at least one digit.
#
#
#
#
# An integer can be split up into these components (in order):
#
#
# (Optional) A sign character (either '+' or '-').
# At least one digit.
#
#
# For example, all the following are valid numbers: ["2", "0089", "-0.1",
# "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
# "-123.456e789"], while the following are not valid numbers: ["abc", "1a",
# "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
#
# Given a string s, return true if s is a valid number.
#
#
# Example 1:
#
#
# Input: s = "0"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "e"
# Output: false
#
#
# Example 3:
#
#
# Input: s = "."
# Output: false
#
#
# Example 4:
#
#
# Input: s = ".1"
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits
# (0-9), plus '+', minus '-', or dot '.'.
#
#
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 判断是否是合法的数字字符串。
# 有限状态自动机 FSA。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        fsa = [
            # d + . e

            # 0 init
            [1, -2, -3, -1],
            # 1 d
            [1, -1, 2, -4],
            # 2 d .
            [3, -1, -1, -4],
            # 3 d . d
            [3, -1, -1, -4],
            # 4 d e d
            [4, -1, -1, -1],


            # -5 d e +
            [4, -1, -1, -1],
            # -4 d e
            [4, -5, -1, -1],
            # -3 .
            [2, -1, -1, -1],
            # -2 +
            [1, -1, -3, -1],
            # -1 error
            [-1, -1, -1, -1],
        ]
        i = 0
        j = -1
        for n in s:
            if '0' <= n <= '9':
                j = 0
            elif n == '+' or n == '-':
                j = 1
            elif n == '.':
                j = 2
            elif n == 'e' or n == 'E':
                j = 3
            else:
                i = -1

            i = fsa[i][j]

            if i == -1:
                return False
        if i <= 0:
            return False
        return True


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "0"')
    print('Output :')
    print(str(Solution().isNumber("0")))
    print('Exception :')
    print('true')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "e"')
    print('Output :')
    print(str(Solution().isNumber("e")))
    print('Exception :')
    print('false')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "."')
    print('Output :')
    print(str(Solution().isNumber(".")))
    print('Exception :')
    print('false')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = ".1"')
    print('Output :')
    print(str(Solution().isNumber(".1")))
    print('Exception :')
    print('true')
    print()
    
    pass
# @lc main=end