# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (67.34%)
# Likes:    4521
# Dislikes: 122
# Total Accepted:    349.2K
# Total Submissions: 514.1K
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return
# 0.
#
#
# Example 1:
#
#
# Input: grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected
# 4-directionally.
#
#
# Example 2:
#
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
#
#
#

# @lc tags=array;depth-first-search

# @lc imports=start
from typing_extensions import get_origin
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最大的岛屿面积。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        direcs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                if grid[i][j] == 0:
                    continue
                resT = 0
                q = [(i, j)]
                while q:
                    i, j = q.pop()
                    resT += 1
                    for oi, oj in direcs:
                        ni, nj = i + oi, j + oj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if (ni, nj) not in visited and grid[ni][nj] == 1:
                                q.append((ni, nj))
                                visited.add((ni, nj))

                res = max(res, resT)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'grid =[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
    )
    print('Exception :')
    print('6')
    print('Output :')
    print(
        str(Solution().maxAreaOfIsland(
            [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,0,0,0,0,0,0,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]])))
    print()

    pass
# @lc main=end