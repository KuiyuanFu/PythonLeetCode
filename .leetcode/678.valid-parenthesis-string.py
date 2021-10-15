# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (32.22%)
# Likes:    2799
# Dislikes: 71
# Total Accepted:    147.4K
# Total Submissions: 455.4K
# Testcase Example:  '"()"'
#
# Given a string s containing only three types of characters: '(', ')' and '*',
# return true if s is valid.
#
# The following rules define a valid string:
#
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis
# ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string "".
#
#
#
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "(*)"
# Output: true
# Example 3:
# Input: s = "(*))"
# Output: true
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 匹配括号，有通配符。
# 栈。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        for c in s:
            if c == ')':
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1][0] == '(' or len(stack) == 1:
                        stack[-1][1] -= 1
                        if stack[-1][1] == 0:
                            stack.pop()
                    else:
                        stack[-2][1] -= 1
                        if stack[-2][1] == 0:
                            if len(stack) >= 3:
                                stack[-3][1] += stack[-1][1]
                                stack.pop()
                            else:
                                stack[-2] = stack[-1]
                            stack.pop()
            else:
                if stack and c == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])
        n = 0
        while stack:
            c, nc = stack.pop()
            if c == '(':
                if n < nc:
                    return False
                n -= nc
            else:
                n += nc
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "()"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkValidString("()")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "(*)"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkValidString("(*)")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "(*))"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkValidString("(*))")))
    print()
    print(str(Solution().checkValidString("(*)))")))
    print(str(Solution().checkValidString("((*)))")))
    print(str(Solution().checkValidString("(((*)))")))
    print(str(Solution().checkValidString("((((*)))")))
    print(str(Solution().checkValidString("()((((*)))")))
    print(str(Solution().checkValidString("()()**((((*)))")))
    print(str(Solution().checkValidString("((((*)(*)))")))
    pass
# @lc main=end