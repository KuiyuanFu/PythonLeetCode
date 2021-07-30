# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (51.75%)
# Likes:    1869
# Dislikes: 278
# Total Accepted:    144.4K
# Total Submissions: 278.9K
# Testcase Example:  '2'
#
# Given an integer n, break it into the sum of k positive integers, where k >=
# 2, and maximize the product of those integers.
#
# Return the maximum product you can get.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#
# Example 2:
#
#
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
#
#
# Constraints:
#
#
# 2 <= n <= 58
#
#
#

# @lc tags=math;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个数，分解成至少两个数的和，之后计算这些数的积，求积的最大值。
# 直接动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self) -> None:

        dp = [i - 1 for i in range(59)]
        dp[:3] = [0, 1, 1]
        for n in range(3, 59):
            for l in range(1, n // 2 + 1):
                r = n - l
                t = max(l, dp[l]) * max(r, dp[r])
                if t > dp[n]:
                    dp[n] = t
        self.dp = dp
        pass

    def integerBreak(self, n: int) -> int:
        return self.dp[n]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().integerBreak(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('36')
    print('Output :')
    print(str(Solution().integerBreak(10)))
    print()

    pass
# @lc main=end