#
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
# @lc idea=start
#
# 给定括号对数量，计算所有合法的括号对。
# 递归，对n-1个括号对的所有合法的组合，将对号插入到所有可能的位置，之后去重。
#
# @lc idea=end

from typing import *
# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        parentheses = set()
        for s in self.generateParenthesis(n-1):
            for i in range(len(s) + 1):
                parentheses.add(s[:i]+'()'+s[i:])
        return list(parentheses)

# @lc code=end


if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
