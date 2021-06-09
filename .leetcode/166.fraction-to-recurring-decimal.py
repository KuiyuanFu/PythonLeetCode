# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (22.55%)
# Likes:    1177
# Dislikes: 2329
# Total Accepted:    153.9K
# Total Submissions: 681.5K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# If multiple answers are possible, return any of them.
#
# It is guaranteed that the length of the answer string is less than 10^4 for
# all the given inputs.
#
#
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# Example 4:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# Example 5:
# Input: numerator = 1, denominator = 5
# Output: "0.2"
#
#
# Constraints:
#
#
# -2^31 <= numerator, denominator <= 2^31 - 1
# denominator != 0
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个整数，即除数和被除数，求商，将小数循环部分以括号包裹的形式给出。
# 使用dict，记录除数，之后看是否有循环。拆分，组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        mem = {}
        buf = []
        # flag
        if numerator * denominator < 0:
            buf.append('-')
        # set positive
        numerator = abs(numerator)
        denominator = abs(denominator)

        # integer
        for c in str(numerator // denominator):
            buf.append(c)
        numerator = numerator % denominator
        buf.append('.')

        # fraction
        while numerator != 0 and numerator not in mem:
            mem[numerator] = len(buf)
            numerator *= 10
            c = str(numerator // denominator)
            buf.append(c)
            numerator = numerator % denominator

        # combine
        r = ''
        if numerator == 0:
            r = ''.join(buf)
        else:
            index = mem[numerator]
            r = ''.join(buf[:index]) + '(' + ''.join(buf[index:]) + ')'
        return r.strip('.')
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numerator = 1, denominator = 2')
    print('Exception :')
    print('"0.5"')
    print('Output :')
    print(str(Solution().fractionToDecimal(1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('numerator = 2, denominator = 1')
    print('Exception :')
    print('"2"')
    print('Output :')
    print(str(Solution().fractionToDecimal(2, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('numerator = 2, denominator = 3')
    print('Exception :')
    print('"0.(6)"')
    print('Output :')
    print(str(Solution().fractionToDecimal(2, 3)))
    print()

    print('Example 4:')
    print('Input : ')
    print('numerator = 4, denominator = 333')
    print('Exception :')
    print('"0.(012)"')
    print('Output :')
    print(str(Solution().fractionToDecimal(4, 333)))
    print()

    print('Example 5:')
    print('Input : ')
    print('numerator = 1, denominator = 5')
    print('Exception :')
    print('"0.2"')
    print('Output :')
    print(str(Solution().fractionToDecimal(1, 5)))
    print()

    pass
# @lc main=end