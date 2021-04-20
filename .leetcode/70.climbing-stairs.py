# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (48.79%)
# Likes:    6377
# Dislikes: 205
# Total Accepted:    940.1K
# Total Submissions: 1.9M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#


# @lc tags=dynamic-programming

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 爬楼梯，每一次可以爬一个台阶或则两个，求有多少种方式到顶。
# 直接动态规划。
# 实际上就是斐波那契数列。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        # 到达第1 ， 2个台阶的方式。
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Output :')
    print(str(Solution().climbStairs(2)))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Output :')
    print(str(Solution().climbStairs(3)))
    print('Exception :')
    print('3')
    print()

    pass
# @lc main=end
