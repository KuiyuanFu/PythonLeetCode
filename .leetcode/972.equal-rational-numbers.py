# @lc app=leetcode id=972 lang=python3
#
# [972] Equal Rational Numbers
#
# https://leetcode.com/problems/equal-rational-numbers/description/
#
# algorithms
# Hard (42.97%)
# Likes:    72
# Dislikes: 191
# Total Accepted:    5.7K
# Total Submissions: 13.3K
# Testcase Example:  '"0.(52)"\n"0.5(25)"'
#
# Given two strings s and t, each of which represents a non-negative rational
# number, return true if and only if they represent the same number. The
# strings may use parentheses to denote the repeating part of the rational
# number.
#
# A rational number can be represented using up to three parts: <IntegerPart>,
# <NonRepeatingPart>, and a <RepeatingPart>. The number will be represented in
# one of the following three ways:
#
#
# <IntegerPart>
#
#
# For example, 12, 0, and 123.
#
#
# <IntegerPart><.><NonRepeatingPart>
#
# For example, 0.5, 1., 2.12, and 123.0001.
#
#
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
#
# For example, 0.1(6), 1.(9), 123.00(1212).
#
#
#
#
# The repeating portion of a decimal expansion is conventionally denoted within
# a pair of round brackets. For example:
#
#
# 1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66).
#
#
#
# Example 1:
#
#
# Input: s = "0.(52)", t = "0.5(25)"
# Output: true
# Explanation: Because "0.(52)" represents 0.52525252..., and "0.5(25)"
# represents 0.52525252525..... , the strings represent the same number.
#
#
# Example 2:
#
#
# Input: s = "0.1666(6)", t = "0.166(66)"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "0.9(9)", t = "1."
# Output: true
# Explanation: "0.9(9)" represents 0.999999999... repeated forever, which
# equals 1.  [See this link for an explanation.]
# "1." represents the number 1, which is formed correctly: (IntegerPart) = "1"
# and (NonRepeatingPart) = "".
#
#
#
# Constraints:
#
#
# Each part consists only of digits.
# The <IntegerPart> does not have leading zeros (except for the zero
# itself).
# 1 <= <IntegerPart>.length <= 4
# 0 <= <NonRepeatingPart>.length <= 4
# 1 <= <RepeatingPart>.length <= 4
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 数字可以有三个部分，一个整数，一个小数，一个循环小数，判断两个数是否相同。
# 变成相同形式，小数和重复部分都变成4位。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def isRationalEqual(self, s: str, t: str) -> bool:

        def format(s: str):
            if s.count('.') == 0:
                i, j, k = s, '0000', '0000'
            else:
                if s.count('(') == 0:
                    i, j = s.split('.')
                    k = '0000'
                else:
                    res = re.match('(.*?)\.(.*?)\((.*?)\)', s)

                    i, j, k = res.group(1), res.group(2), res.group(3)
                    if k.count(k[0]) == len(k):
                        k = k[0]

                while len(j) < 4:

                    j = j + k[0]
                    k = k[1:] + k[0]
                if len(k) == 1:
                    k = k * 4
                elif len(k) == 2:
                    k = k * 2
                if k.count('9') == 4:
                    k = '0000'
                    j = str(int(j) + 1)
                    j = '0' * (4 - len(j)) + j

                    if len(j) == 5:
                        j = j[1:]
                        i = str(int(i) + 1)

            return (i, j, k)
            pass

        s, t = format(s), format(t)
        return s == t
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "0.(52)", t = "0.5(25)"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isRationalEqual("0.(52)", "0.5(25)")))
    print()
    print('Example 1:')
    print('Input : ')
    print('s = "0.08(9)", t = "0.09"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isRationalEqual("0.08(9)", "0.09")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "0.1666(6)", t = "0.166(66)"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isRationalEqual("0.1666(6)", "0.166(66)")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "0.9(9)", t = "1."')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isRationalEqual("0.9(9)", "1.")))
    print(str(Solution().isRationalEqual("350.(111)", "350.(11)")))
    print(str(Solution().isRationalEqual("350.(350)", "350.350(350)")))
    print()

    pass
# @lc main=end