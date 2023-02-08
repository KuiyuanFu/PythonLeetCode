# @lc app=leetcode id=1034 lang=python3
#
# [1034] Coloring A Border
#
# https://leetcode.com/problems/coloring-a-border/description/
#
# algorithms
# Medium (49.12%)
# Likes:    579
# Dislikes: 756
# Total Accepted:    28.4K
# Total Submissions: 57.8K
# Testcase Example:  '[[1,1],[1,2]]\n0\n0\n3'
#
# You are given an m x n integer matrix grid, and three integers row, col, and
# color. Each value in the grid represents the color of the grid square at that
# location.
#
# Two squares belong to the same connected component if they have the same
# color and are next to each other in any of the 4 directions.
#
# The border of a connected component is all the squares in the connected
# component that are either 4-directionally adjacent to a square not in the
# component, or on the boundary of the grid (the first or last row or column).
#
# You should color the border of the connected component that contains the
# square grid[row][col] with color.
#
# Return the final grid.
#
#
# Example 1:
# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]
# Example 2:
# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]
# Example 3:
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n
#
#
#

# @lc tags=hash-table;two-pointers;sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二维网格，相邻同一颜色为一个部分，给定一个位置，将这个位置所属的部分的边界改为指定颜色
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def colorBorder(self, grid: List[List[int]], row: int, col: int,
                    color: int) -> List[List[int]]:

        cc = grid[row][col]
        r, c = len(grid), len(grid[0])

        q = [(row, col)]
        visited = set(q)
        os = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ns = []
        while q:
            i, j = q.pop()
            f = False
            for oi, oj in os:
                ni, nj = i + oi, j + oj
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == cc:

                    if (ni, nj) not in visited:
                        q.append((ni, nj))
                        visited.add((ni, nj))

                else:
                    f = True
            if f:
                ns.append((i, j))
        for i, j in ns:
            grid[i][j] = color
        return grid
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,1],[1,2]], row = 0, col = 0, color = 3')
    print('Exception :')
    print('[[3,3],[3,2]]')
    print('Output :')
    print(str(Solution().colorBorder([[1, 1], [1, 2]], 0, 0, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3')
    print('Exception :')
    print('[[1,3,3],[2,3,3]]')
    print('Output :')
    print(str(Solution().colorBorder([[1, 2, 2], [2, 3, 2]], 0, 1, 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2')
    print('Exception :')
    print('[[2,2,2],[2,1,2],[2,2,2]]')
    print('Output :')
    print(
        str(Solution().colorBorder([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1,
                                   2)))
    print()

    pass
# @lc main=end