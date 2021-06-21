# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (39.04%)
# Likes:    2508
# Dislikes: 381
# Total Accepted:    280.4K
# Total Submissions: 716.2K
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value.
#
# The integer division should truncate toward zero.
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个有效表达式，求解。
# 直接用栈即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s + '+'

        nums = [0, 0]
        operators = [('+')]

        def cal(flag):
            while operators:
                operator = operators.pop()
                num2 = nums.pop()
                num1 = nums.pop()
                if operator == '+':
                    nums.append(num1 + num2)
                elif operator == '-':
                    nums.append(num1 - num2)
                elif operator == '*':
                    nums.append(num1 * num2)
                elif operator == '/':
                    nums.append(num1 // num2)
                if not flag:
                    return

        def getLevel(c):
            lever = 0
            if c == '+' or c == '-':
                lever = 1
            return lever

        for c in s:
            if '0' <= c <= '9':
                nums[-1] = nums[-1] * 10 + ord(c) - ord('0')
            elif c != ' ':
                lever = getLevel(c)
                while operators:
                    targetLever = getLevel(operators[-1])
                    if targetLever <= lever:
                        operator = operators.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        if operator == '+':
                            nums.append(num1 + num2)
                        elif operator == '-':
                            nums.append(num1 - num2)
                        elif operator == '*':
                            nums.append(num1 * num2)
                        elif operator == '/':
                            nums.append(num1 // num2)
                    else:
                        break
                operators.append(c)
                nums.append(0)
        return nums[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "3+2*2"')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().calculate("3+2*2")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = " 3/2 "')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().calculate(" 3/2 ")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = " 3+5 / 2 "')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().calculate(" 3+5 / 2 ")))
    print()

    pass
# @lc main=end