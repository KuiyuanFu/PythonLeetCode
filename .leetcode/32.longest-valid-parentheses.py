# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (29.87%)
# Likes:    5043
# Dislikes: 182
# Total Accepted:    367.9K
# Total Submissions: 1.2M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
#
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
#
#
#
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个只含有左右括号的字符串，求最长有效括号。
# 使用栈和一个临时变量，临时变量表示当前合法的长度，每遇到一个左括号，将临时变量入栈，即若匹配这个左括号，就会增加的额外长度。
# 每次遇到右括号，检查栈是否为空，若为空，则匹配失败，长度置为0；若栈中不为空，则长度增加2及栈中的值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        lengthMax = 0
        length = 0

        for c in s:
            if c == '(':
                stack.append(length)
                length = 0
            else:
                if len(stack) != 0:
                    length += 2 + stack.pop()
                    if length > lengthMax:
                        lengthMax = length
                else:
                    length = 0

        return lengthMax
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "(()"')
    print('Output :')
    print(str(Solution().longestValidParentheses("(()")))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('s = ")()())"')
    print('Output :')
    print(str(Solution().longestValidParentheses(")()())")))
    print('Exception :')
    print('4')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = ""')
    print('Output :')
    print(str(Solution().longestValidParentheses("")))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end