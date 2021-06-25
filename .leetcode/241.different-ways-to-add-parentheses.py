# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (57.97%)
# Likes:    2279
# Dislikes: 122
# Total Accepted:    125.9K
# Total Submissions: 216.4K
# Testcase Example:  '"2-1-1"'
#
# Given a string expression of numbers and operators, return all possible
# results from computing all the different possible ways to group numbers and
# operators. You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
#
# Example 2:
#
#
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#
#
# Constraints:
#
#
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
#
#
#

# @lc tags=divide-and-conquer

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个表达式，返回以所有顺序的结果。
# 直接动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expression += '-'
        nums = []
        operaters = []
        n = 0
        for c in expression:
            if '0' <= c <= '9':
                n = 10 * n + ord(c) - ord('0')
            else:
                nums.append(n)
                n = 0
                if c == '+':
                    f = lambda x, y: x + y
                elif c == '-':
                    f = lambda x, y: x - y
                elif c == '*':
                    f = lambda x, y: x * y
                operaters.append(f)
        n = len(nums)

        dp = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].append(nums[i])

        for step in range(2, n + 1):
            for i in range(n - step + 1):
                j = i + step - 1
                for m in range(i, i + step - 1):
                    lSet = dp[i][m]
                    rSet = dp[m + 1][j]
                    f = operaters[m]
                    for l in lSet:
                        for r in rSet:
                            dp[i][j].append(f(l, r))
        return dp[0][-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('expression = "2-1-1"')
    print('Exception :')
    print('[0,2]')
    print('Output :')
    print(str(Solution().diffWaysToCompute("2-1-1")))
    print()

    print('Example 2:')
    print('Input : ')
    print('expression = "2*3-4*5"')
    print('Exception :')
    print('[-34,-14,-10,-10,10]')
    print('Output :')
    print(str(Solution().diffWaysToCompute("2*3-4*5")))
    print()

    pass
# @lc main=end