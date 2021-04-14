#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (56.46%)
# Likes:    4567
# Dislikes: 83
# Total Accepted:    527.8K
# Total Submissions: 934K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
# 
# 
#
# 
#
# @lc idea=start
#
# 求加权最短路径代价。
# 动态规划.
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)-2,-1,-1):
            grid[i][-1] += grid[i+1][-1] 
        for j in range(len(grid[0])-2,-1,-1):
            grid[-1][j] += grid[-1][j+1] 
        for i in range(len(grid)-2,-1,-1):
            for j in range(len(grid[0])-2,-1,-1):
                grid[i][j] += grid[i+1][j] if grid[i+1][j] < grid[i][j+1] else grid[i][j+1]
        return grid[0][0]
# @lc code=end

