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
# 统计方法。统计有多少个左括号在通配符的右侧。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        # number of *
        ns = 0
        # number of (
        np = 0
        # number of ( right than *
        nprs = 0
        for c in s:
            if c == '(':
                ns += 1
                nprs += 1
            elif c == '*':
                np += 1
                nprs = max(0, nprs - 1)
            else:
                if ns > 0:
                    ns -= 1
                    nprs = max(0, nprs - 1)
                elif np > 0:
                    np -= 1
                else:
                    return False
        return nprs == 0


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