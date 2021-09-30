# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#
# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (51.04%)
# Likes:    265
# Dislikes: 403
# Total Accepted:    25.9K
# Total Submissions: 50.7K
# Testcase Example:  '"-1/2+1/2"'
#
# Given a string expression representing an expression of fraction addition and
# subtraction, return the calculation result in string format.
#
# The final result should be an irreducible fraction. If your final result is
# an integer, say 2, you need to change it to the format of a fraction that has
# a denominator 1. So in this case, 2 should be converted to 2/1.
#
#
# Example 1:
#
#
# Input: expression = "-1/2+1/2"
# Output: "0/1"
#
#
# Example 2:
#
#
# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
#
#
# Example 3:
#
#
# Input: expression = "1/3-1/2"
# Output: "-1/6"
#
#
# Example 4:
#
#
# Input: expression = "5/3+1/3"
# Output: "2/1"
#
#
#
# Constraints:
#
#
# The input string only contains '0' to '9', '/', '+' and '-'. So does the
# output.
# Each fraction (input and output) has the format ±numerator/denominator. If
# the first input fraction or the output is positive, then '+' will be
# omitted.
# The input only contains valid irreducible fractions, where the numerator and
# denominator of each fraction will always be in the range [1, 10]. If the
# denominator is 1, it means this fraction is actually an integer in a fraction
# format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid
# and in the range of 32-bit int.
#
#
#

# @lc tags=math

# @lc imports=start
import functools
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将分数表达式化为最简形式。
# 欧几里得除法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        from functools import reduce
        expression += '+'
        d = [0] * 11
        s = []
        for c in expression:
            if c == '/':
                numerator = int(''.join(s))
                s.clear()
            else:
                if (c == '+' or c == '-') and s:
                    denominator = int(''.join(s))
                    d[denominator] += numerator
                    s.clear()
                s.append(c)

        def gcd(a, b):
            c = a % b
            while c != 0:
                a, b = b, c
                c = a % b
            return b

        def lcm(a, b):
            g = gcd(a, b)
            return a // g * b

        numeratorAll = 0
        denominatorAll = 1
        for denominator, numerator in enumerate(d):
            if numerator != 0:
                denominatorAll = lcm(denominatorAll, denominator)
        for denominator, numerator in enumerate(d):
            if numerator != 0:
                numeratorAll += denominatorAll // denominator * numerator
        if numeratorAll == 0:
            return '0/1'
        g = gcd(numeratorAll, denominatorAll)
        return '{}/{}'.format(numeratorAll // g, denominatorAll // g)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('expression = "-1/2+1/2"')
    print('Exception :')
    print('"0/1"')
    print('Output :')
    print(str(Solution().fractionAddition("-1/2+1/2")))
    print()

    print('Example 2:')
    print('Input : ')
    print('expression = "-1/2+1/2+1/3"')
    print('Exception :')
    print('"1/3"')
    print('Output :')
    print(str(Solution().fractionAddition("-1/2+1/2+1/3")))
    print()

    print('Example 3:')
    print('Input : ')
    print('expression = "1/3-1/2"')
    print('Exception :')
    print('"-1/6"')
    print('Output :')
    print(str(Solution().fractionAddition("1/3-1/2")))
    print()

    print('Example 4:')
    print('Input : ')
    print('expression = "5/3+1/3"')
    print('Exception :')
    print('"2/1"')
    print('Output :')
    print(str(Solution().fractionAddition("5/3+1/3")))
    print()

    pass
# @lc main=end