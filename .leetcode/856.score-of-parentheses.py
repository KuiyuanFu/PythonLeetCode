# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (65.41%)
# Likes:    4253
# Dislikes: 135
# Total Accepted:    133K
# Total Submissions: 203.1K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string s, return the score of the string.
#
# The score of a balanced parentheses string is based on the following
# rule:
#
#
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: 1
#
#
# Example 2:
#
#
# Input: s = "(())"
# Output: 2
#
#
# Example 3:
#
#
# Input: s = "()()"
# Output: 2
#
#
#
# Constraints:
#
#
# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 括号分数
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s = '(' + s + ')'

        def recur(idx):
            score = 0
            while True:
                if s[idx] == ')':
                    break
                sn, idx = recur(idx + 1)
                score += sn
            return (1 if score == 0 else 2 * score), idx + 1

        return recur(0 + 1)[0] // 2
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "()"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().scoreOfParentheses("()")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "(())"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().scoreOfParentheses("(())")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "()()"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().scoreOfParentheses("()()")))
    print()

    pass
# @lc main=end