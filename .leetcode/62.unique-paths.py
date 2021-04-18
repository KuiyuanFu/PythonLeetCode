# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (56.30%)
# Likes:    4903
# Dislikes: 241
# Total Accepted:    624.9K
# Total Submissions: 1.1M
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
#
#
# Example 2:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
# Example 3:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#
# Example 4:
#
#
# Input: m = 3, n = 3
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.
#
#
#
#
#

# @lc tags=array;dynamic-programming

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 在一个board 上，只能向右或下走，从左上到右下有多少种路径。
# dp。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m]*2
        for _ in range(n - 1):
            dp[1], dp[0] = dp[0], dp[1]
            for j in range(1, m):
                dp[1][j] = dp[0][j] + dp[1][j-1]
        return dp[1][-1]


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('m = 3, n = 7')
    print('Output :')
    print(str(Solution().uniquePaths(3,7)))
    print('Exception :')
    print('28')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('m = 3, n = 2')
    print('Output :')
    print(str(Solution().uniquePaths(3,2)))
    print('Exception :')
    print('3')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('m = 7, n = 3')
    print('Output :')
    print(str(Solution().uniquePaths(7,3)))
    print('Exception :')
    print('28')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('m = 3, n = 3')
    print('Output :')
    print(str(Solution().uniquePaths(3,3)))
    print('Exception :')
    print('6')
    print()
    
    pass
# @lc main=end