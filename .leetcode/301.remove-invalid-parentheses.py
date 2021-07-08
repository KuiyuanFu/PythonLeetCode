# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (45.12%)
# Likes:    3581
# Dislikes: 166
# Total Accepted:    278.2K
# Total Submissions: 613.9K
# Testcase Example:  '"()())()"'
#
# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
#
# Return all the possible results. You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "()())()"
# Output: ["(())()","()()()"]
#
#
# Example 2:
#
#
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
#
#
# Example 3:
#
#
# Input: s = ")("
# Output: [""]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
#
#
#

# @lc tags=depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个括号和字母组成的字符串，括号匹配可能有问题，最小移除次数，使括号合法。
# 直接深度优先全局遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ret = set()

        def rRemoveInvalidParentheses(index, count, prefix):
            if index == len(s):
                if count == 0:
                    length = len(prefix)
                    if len(ret) == 0 or length >= len(next(iter(ret), '')):
                        ret.add(prefix)
                    else:
                        return False
                return True
            c = s[index]
            if c == '(':
                rRemoveInvalidParentheses(index + 1, count + 1, prefix + c)
                rRemoveInvalidParentheses(index + 1, count, prefix)

            elif c == ')':
                if count > 0:
                    r = rRemoveInvalidParentheses(index + 1, count - 1,
                                                  prefix + c)
                rRemoveInvalidParentheses(index + 1, count, prefix)

            else:
                rRemoveInvalidParentheses(index + 1, count, prefix + c)

        rRemoveInvalidParentheses(0, 0, '')
        return list(ret)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "()())()"')
    print('Exception :')
    print('["(())()","()()()"]')
    print('Output :')
    print(str(Solution().removeInvalidParentheses("()())()")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "(a)())()"')
    print('Exception :')
    print('["(a())()","(a)()()"]')
    print('Output :')
    print(str(Solution().removeInvalidParentheses("(a)())()")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = ")("')
    print('Exception :')
    print('[""]')
    print('Output :')
    print(str(Solution().removeInvalidParentheses(")(")))
    print()

    pass
# @lc main=end