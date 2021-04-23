# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.98%)
# Likes:    7219
# Dislikes: 297
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: s = "{[]}"
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#
#

# @lc tags=string;stack

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 判断括号是否匹配.
# 使用栈或者递归都可以，思想是一致的，栈比较快。
# 读取到一个左括号，就压栈，否者就弹出一个，看是否匹配。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        ls = ['(', '[', '{', ]
        rs = [')', ']', '}', ]
        stack = []
        for c in s:
            if c in ls:
                stack.append(c)
            elif len(stack) == 0 or ls.index(stack.pop()) != rs .index(c):
                return False

        return True if len(stack) == 0 else False

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "()"')
    print('Output :')
    print(str(Solution().isValid("()")))
    print('Exception :')
    print('true')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "()[]{}"')
    print('Output :')
    print(str(Solution().isValid("()[]{}")))
    print('Exception :')
    print('true')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "(]"')
    print('Output :')
    print(str(Solution().isValid("(]")))
    print('Exception :')
    print('false')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = "([)]"')
    print('Output :')
    print(str(Solution().isValid("([)]")))
    print('Exception :')
    print('false')
    print()
    
    print('Example 5:')
    print('Input : ')
    print('s = "{[]}"')
    print('Output :')
    print(str(Solution().isValid("{[]}")))
    print('Exception :')
    print('true')
    print()
    
    pass
# @lc main=end