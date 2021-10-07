# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#
# https://leetcode.com/problems/solve-the-equation/description/
#
# algorithms
# Medium (43.07%)
# Likes:    319
# Dislikes: 642
# Total Accepted:    30K
# Total Submissions: 69.5K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
# Solve a given equation and return the value of 'x' in the form of a string
# "x=#value". The equation contains only '+', '-' operation, the variable 'x'
# and its coefficient. You should return "No solution" if there is no solution
# for the equation, or "Infinite solutions" if there are infinite solutions for
# the equation.
#
# If there is exactly one solution for the equation, we ensure that the value
# of 'x' is an integer.
#
#
# Example 1:
# Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:
# Input: equation = "x=x"
# Output: "Infinite solutions"
# Example 3:
# Input: equation = "2x=x"
# Output: "x=0"
# Example 4:
# Input: equation = "2x+3x-6x=x+2"
# Output: "x=-1"
# Example 5:
# Input: equation = "x=x+2"
# Output: "No solution"
#
#
# Constraints:
#
#
# 3 <= equation.length <= 1000
# equation has exactly one '='.
# equation consists of integers with an absolute value in the range [0, 100]
# without any leading zeros, and the variable 'x'.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 解方程。
# 简单解析公式字符串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split('=')

        def parse(s):
            s += '+'
            pre = ''
            xn = 0
            cn = 0
            for c in s:
                if c == '+' or c == '-':
                    if len(pre) != 0:
                        if pre[-1] == 'x':
                            pre = pre[:len(pre) - 1]

                            if len(pre) == 0:
                                xn += 1
                            else:
                                if pre == '+' or pre == '-':
                                    pre += '1'
                                xn += int(pre)
                        else:
                            cn += int(pre)
                        pre = ''

                pre += c
            return xn, cn

        lxn, lcn = parse(l)
        rxn, rcn = parse(r)
        xn = lxn - rxn
        cn = rcn - lcn
        if xn == 0:
            if cn == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            value = cn // xn
            return 'x={}'.format(value)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('equation = "x+5-3+x=6+x-2"')
    print('Exception :')
    print('"x=2"')
    print('Output :')
    print(str(Solution().solveEquation("x+5-3+x=6+x-2")))
    print()

    print('Example 2:')
    print('Input : ')
    print('equation = "x=x"')
    print('Exception :')
    print('"Infinite solutions"')
    print('Output :')
    print(str(Solution().solveEquation("x=x")))
    print()

    print('Example 3:')
    print('Input : ')
    print('equation = "2x=x"')
    print('Exception :')
    print('"x=0"')
    print('Output :')
    print(str(Solution().solveEquation("2x=x")))
    print()

    print('Example 4:')
    print('Input : ')
    print('equation = "2x+3x-6x=x+2"')
    print('Exception :')
    print('"x=-1"')
    print('Output :')
    print(str(Solution().solveEquation("2x+3x-6x=x+2")))
    print()

    print('Example 5:')
    print('Input : ')
    print('equation = "x=x+2"')
    print('Exception :')
    print('"No solution"')
    print('Output :')
    print(str(Solution().solveEquation("x=x+2")))
    print()

    pass
# @lc main=end