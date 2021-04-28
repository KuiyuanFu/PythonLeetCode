# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (65.70%)
# Likes:    7525
# Dislikes: 324
# Total Accepted:    716.6K
# Total Submissions: 1.1M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#
#

# @lc tags=string;backtracking

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定括号对数量，计算所有合法的括号对。
# 递归，对n-1个括号对的所有合法的组合，将括号插入到所有可能的位置，之后去重。
# 最初的想法是，将n-1个括号对的所有合法的组合插入的一个括号的左中右三个位置上，但是发现有的情况不能覆盖。当 n 为 4 时，'(())(())' 就不会被覆盖。这种想法是错误的。
#
# @lc idea=end

# @lc group=parentheses

# @lc rank=10

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        parentheses = set()
        for s in self.generateParenthesis(n - 1):
            for i in range(len(s) + 1):
                parentheses.add(s[:i] + '()' + s[i:])
        return list(parentheses)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Output :')
    print(str(Solution().generateParenthesis(3)))
    print('Exception :')
    print('["((()))","(()())","(())()","()(())","()()()"]')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().generateParenthesis(1)))
    print('Exception :')
    print('["()"]')
    print()

    pass
# @lc main=end