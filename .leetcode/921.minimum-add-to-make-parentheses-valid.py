# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (77.16%)
# Likes:    2533
# Dislikes: 145
# Total Accepted:    210.1K
# Total Submissions: 272.7K
# Testcase Example:  '"())"'
#
# A parentheses string is valid if and only if:
#
#
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
#
#
# You are given a parentheses string s. In one move, you can insert a
# parenthesis at any position of the string.
#
#
# For example, if s = "()))", you can insert an opening parenthesis to be
# "(()))" or a closing parenthesis to be "())))".
#
#
# Return the minimum number of moves required to make s valid.
#
#
# Example 1:
#
#
# Input: s = "())"
# Output: 1
#
#
# Example 2:
#
#
# Input: s = "((("
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最少插入次数，使括号可用。
# 直接遍历，统计左括号个数，如果遇到右括号时，没有左括号，那么就必须插入一个左括号。最后若剩余左括号，就必须插入右括号。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        # leftParentheses
        lp = 0
        for c in s:
            if c == '(':
                lp += 1
            else:
                if lp > 0:
                    lp -= 1
                else:
                    res += 1
        res += lp
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "())"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minAddToMakeValid("())")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "((("')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minAddToMakeValid("(((")))
    print()

    pass
# @lc main=end