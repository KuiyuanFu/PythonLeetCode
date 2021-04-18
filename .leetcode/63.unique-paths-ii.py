# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (35.37%)
# Likes:    2630
# Dislikes: 291
# Total Accepted:    363.1K
# Total Submissions: 1M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# An obstacle and space is marked as 1 and 0 respectively in the grid.
# 
# 
# Example 1:
# 
# 
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
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
# 有障碍的路径个数。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 直接是石头
        if obstacleGrid[-1][-1] == 1:
            return 0 
        # 直接可以得到
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            return 1
        # 初始化最右侧
        for i in range(len(obstacleGrid)-2,-1,-1):
            if obstacleGrid[i][-1]==0 :
                obstacleGrid[i][-1]  = 1 if obstacleGrid[i+1][-1] == 1 else -1 
        # 初始化最下侧
        for j in range(len(obstacleGrid[0])-2,-1,-1):
            if obstacleGrid[-1][j]==0 :
                obstacleGrid[-1][j] = 1 if obstacleGrid[-1][j+1] == 1 else -1    
        # 动态规划     
        for i in range(len(obstacleGrid) -2 ,-1,-1):
            for j in range(len(obstacleGrid[0])-2 ,-1,-1):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] += obstacleGrid[i+1][j] if  obstacleGrid[i+1][j] <0 else 0
                    obstacleGrid[i][j] += obstacleGrid[i][j+1] if  obstacleGrid[i][j+1] <0 else 0
        return -1 * obstacleGrid[0][0] if obstacleGrid[0][0]<= 0 else 0
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]')
    print('Output :')
    print(str(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])))
    print('Exception :')
    print('2')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('obstacleGrid = [[0,1],[0,0]]')
    print('Output :')
    print(str(Solution().uniquePathsWithObstacles([[0,1],[0,0]])))
    print('Exception :')
    print('1')
    print()
    
    pass
# @lc main=end