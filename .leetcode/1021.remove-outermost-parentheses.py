# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
# https://leetcode.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (80.14%)
# Likes:    1640
# Dislikes: 1285
# Total Accepted:    193.7K
# Total Submissions: 241.7K
# Testcase Example:  '"(()())(())"'
#
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where
# A and B are valid parentheses strings, and + represents string
# concatenation.
#
#
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses
# strings.
#
#
# A valid parentheses string s is primitive if it is nonempty, and there does
# not exist a way to split it into s = A + B, with A and B nonempty valid
# parentheses strings.
#
# Given a valid parentheses string s, consider its primitive decomposition: s =
# P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
#
# Return s after removing the outermost parentheses of every primitive string
# in the primitive decomposition of s.
#
#
# Example 1:
#
#
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" =
# "()()()".
#
#
# Example 2:
#
#
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition
# "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" +
# "()(())" = "()()()()(())".
#
#
# Example 3:
#
#
# Input: s = "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either '(' or ')'.
# s is a valid parentheses string.
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 移除最外侧的括号。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        res = []
        p = 0
        for c in s:
            if c == '(':
                if p != 0:
                    res.append(c)

                p += 1
            else:
                if p != 1:
                    res.append(c)
                p -= 1
        return ''.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "(()())(())"')
    print('Exception :')
    print('"()()()"')
    print('Output :')
    print(str(Solution().removeOuterParentheses("(()())(())")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "(()())(())(()(()))"')
    print('Exception :')
    print('"()()()()(())"')
    print('Output :')
    print(str(Solution().removeOuterParentheses("(()())(())(()(()))")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "()()"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().removeOuterParentheses("()()")))
    print()

    pass
# @lc main=end