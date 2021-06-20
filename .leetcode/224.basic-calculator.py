# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.43%)
# Likes:    2347
# Dislikes: 208
# Total Accepted:    217.2K
# Total Submissions: 563.4K
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
# Example 1:
#
#
# Input: s = "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
#
# Example 3:
#
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
# Example 4:
#
#
# Input: s = "+48 + -48"
# Output: 0
# Explanation: Numbers can have multiple digits and start with +/-.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# Every number and running calculation will fit in a signed 32-bit integer.
#
#
#

# @lc tags=math;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个有效表达式，求解。
# 递归，判断是否为符号。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s + '+'
        length = len(s)

        def recur(i):
            r = 0
            # True is '+'
            operator = True

            flag = True
            t = 0

            while i < length:
                if s[i] == '-' or s[i] == '+' or s[i] == '(' or s[
                        i] == ')' or s[i] == ' ':
                    if flag:
                        if operator:
                            r += t
                        else:
                            r -= t
                        t = 0
                        operator = True
                    flag = False
                    if s[i] == '-':
                        operator = not operator
                    elif s[i] == ')':
                        return i, r
                    elif s[i] == '(':
                        i, t = recur(i + 1)
                        flag = True
                else:
                    t = t * 10 + int(s[i])
                    flag = True
                i += 1
            return i, r

        return recur(0)[1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "1 + 1"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().calculate("1 + 1")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = " 2-1 + 2 "')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().calculate(" 2-1 + 2 ")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "(1+(4+5+2)-3)+(6+8)"')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().calculate("(1+(4+5+2)-3)+(6+8)")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "+48 + -48"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().calculate("+48 + -48")))
    print()

    pass
# @lc main=end