# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (67.52%)
# Likes:    3226
# Dislikes: 161
# Total Accepted:    295.2K
# Total Submissions: 436.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
#
#
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#
# Example 2:
#
#
# Input: grid = [[1]]
# Output: 4
#
#
# Example 3:
#
#
# Input: grid = [[1,0]]
# Output: 4
#
#
#
# Constraints:
#
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求岛屿的周长。
# 遍历，根据左上两边是否连接岛屿，确定周长。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        # previous row
        preRow = [0] * cols
        for i in range(rows):
            thisRow = grid[i]
            # left value
            preC = 0
            for j in range(cols):
                g = thisRow[j]
                if g == 1:
                    #          left edge       up edge
                    res += 4 - 2 * preC - 2 * preRow[j]
                preC = g
            preRow = grid[i]
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]')
    print('Exception :')
    print('16')
    print('Output :')
    print(
        str(Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0],
                                        [0, 1, 0, 0], [1, 1, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().islandPerimeter([[1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().islandPerimeter([[1, 0]])))
    print()

    pass
# @lc main=end