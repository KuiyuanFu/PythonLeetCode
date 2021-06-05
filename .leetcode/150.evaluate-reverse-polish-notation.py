# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (39.45%)
# Likes:    1811
# Dislikes: 542
# Total Accepted:    304.8K
# Total Submissions: 771.6K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
#
# Note that division between two integers should truncate toward zero.
#
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
#
#
# Example 1:
#
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
# Constraints:
#
#
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
#
#
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算RPN表达式，即运算符的操作数在其的前面。
# 直接用栈。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                a = stack.pop()
                b = stack.pop()
                flag = -1 if a * b < 0 else 1
                stack.append(flag * (abs(b) // abs(a)))
            else:
                stack.append(int(t))
        return stack[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('tokens = ["2","1","+","3","*"]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().evalRPN(["2", "1", "+", "3", "*"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('tokens = ["4","13","5","/","+"]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().evalRPN(["4", "13", "5", "/", "+"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]')
    print('Exception :')
    print('22')
    print('Output :')
    print(
        str(Solution().evalRPN([
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
        ])))
    print()

    pass
# @lc main=end