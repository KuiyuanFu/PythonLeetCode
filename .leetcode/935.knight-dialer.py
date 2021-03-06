# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#
# https://leetcode.com/problems/knight-dialer/description/
#
# algorithms
# Medium (49.17%)
# Likes:    1551
# Dislikes: 358
# Total Accepted:    81.9K
# Total Submissions: 166.2K
# Testcase Example:  '1'
#
# The chess knight has a unique movement, it may move two squares vertically
# and one square horizontally, or two squares horizontally and one square
# vertically (with both forming the shape of an L). The possible movements of
# chess knight are shown in this diagaram:
#
# A chess knight can move as indicated in the chess diagram below:
#
# We have a chess knight and a phone pad as shown below, the knight can only
# stand on a numeric cell (i.e. blue cell).
#
# Given an integer n, return how many distinct phone numbers of length n we can
# dial.
#
# You are allowed to place the knight on any numeric cell initially and then
# you should perform n - 1 jumps to dial a number of length n. All jumps should
# be valid knight jumps.
#
# As the answer may be very large, return the answer modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over
# any numeric cell of the 10 cells is sufficient.
#
#
# Example 2:
#
#
# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29,
# 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
#
#
# Example 3:
#
#
# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.
#
#
#
# Constraints:
#
#
# 1 <= n <= 5000
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 按键排列个数，满足每一位是日字走法。
# dp，记录末尾数字的排列个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def knightDialer(self, n: int) -> int:

        dp = [1] * 10
        for _ in range(n - 1):
            dp = [
                dp[4] + dp[6],
                dp[8] + dp[6],
                dp[7] + dp[9],
                dp[4] + dp[8],
                dp[3] + dp[9] + dp[0],
                0,
                dp[1] + dp[7] + dp[0],
                dp[2] + dp[6],
                dp[1] + dp[3],
                dp[2] + dp[4],
            ]

        return sum(dp) % 1000000007

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().knightDialer(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().knightDialer(2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 3131')
    print('Exception :')
    print('136006598')
    print('Output :')
    print(str(Solution().knightDialer(3131)))
    print()

    pass
# @lc main=end