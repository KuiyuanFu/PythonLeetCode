# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.11%)
# Likes:    8760
# Dislikes: 249
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#

# @lc tags=depth-first-search;breadth-first-search;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二维数组，0表示水，1表示陆地，求岛屿个数。
# 直接广度优先遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def extend(self, i, j):
        if not (0 <= i < self.rows and 0 <= j < self.cols):
            return
        if self.grid[i][j] == '0':
            return
        else:
            self.grid[i][j] = '0'
        self.extend(i + 1, j)
        self.extend(i - 1, j)
        self.extend(i, j + 1)
        self.extend(i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid
        result = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == '1':
                    result += 1
                    self.extend(i, j)
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 1:')
    print('Input : ')
    print(
        'grid = [⁠ ["1","1","1","1","0"],⁠ ["1","1","0","1","0"],⁠ ["1","1","0","0","0"],⁠ ["0","0","0","0","0"]]'
    )
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().numIslands([["1", "1", "1", "1", "0"],
                                   ["1", "1", "0", "1", "0"],
                                   ["1", "1", "0", "0", "0"],
                                   ["0", "0", "0", "0", "0"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'grid = [⁠ ["1","1","0","0","0"],⁠ ["1","1","0","0","0"],⁠ ["0","0","1","0","0"],⁠ ["0","0","0","1","1"]]'
    )
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numIslands([["1", "1", "0", "0", "0"],
                                   ["1", "1", "0", "0", "0"],
                                   ["0", "0", "1", "0", "0"],
                                   ["0", "0", "0", "1", "1"]])))

    print()
    pass
# @lc main=end