# @lc app=leetcode id=883 lang=python3
#
# [883] Projection Area of 3D Shapes
#
# https://leetcode.com/problems/projection-area-of-3d-shapes/description/
#
# algorithms
# Easy (69.94%)
# Likes:    388
# Dislikes: 1139
# Total Accepted:    40K
# Total Submissions: 57.2K
# Testcase Example:  '[[1,2],[3,4]]'
#
# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are
# axis-aligned with the x, y, and z axes.
#
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the
# cell (i, j).
#
# We view the projection of these cubes onto the xy, yz, and zx planes.
#
# A projection is like a shadow, that maps our 3-dimensional figure to a
# 2-dimensional plane. We are viewing the "shadow" when looking at the cubes
# from the top, the front, and the side.
#
# Return the total area of all three projections.
#
#
# Example 1:
#
#
# Input: grid = [[1,2],[3,4]]
# Output: 17
# Explanation: Here are the three projections ("shadows") of the shape made
# with each axis-aligned plane.
#
#
# Example 2:
#
#
# Input: grid = [[2]]
# Output: 5
#
#
# Example 3:
#
#
# Input: grid = [[1,0],[0,2]]
# Output: 8
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] <= 50
#
#
#

# @lc tags=sort

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计三视图面积和。
# 直接遍历，底面取值是否大于零，侧面取最大值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        rowMax = [0] * row
        colMax = [0] * col
        for i, j in product(range(row), range(col)):
            v = grid[i][j]
            rowMax[i] = max(rowMax[i], v)
            colMax[j] = max(colMax[j], v)
            res += 1 if v > 0 else 0
        res += sum(rowMax) + sum(colMax)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,2],[3,4]]')
    print('Exception :')
    print('17')
    print('Output :')
    print(str(Solution().projectionArea([[1, 2], [3, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[2]]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().projectionArea([[2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,0],[0,2]]')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().projectionArea([[1, 0], [0, 2]])))
    print()

    pass
# @lc main=end