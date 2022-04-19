# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
# https://leetcode.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (61.76%)
# Likes:    405
# Dislikes: 567
# Total Accepted:    28.2K
# Total Submissions: 45.7K
# Testcase Example:  '[[1,2],[3,4]]'
#
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each
# value v = grid[i][j] represents a tower of v cubes placed on top of cell (i,
# j).
#
# After placing these cubes, you have decided to glue any directly adjacent
# cubes to each other, forming several irregular 3D shapes.
#
# Return the total surface area of the resulting shapes.
#
# Note: The bottom face of each shape counts toward its surface area.
#
#
# Example 1:
#
#
# Input: grid = [[1,2],[3,4]]
# Output: 34
#
#
# Example 2:
#
#
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
#
#
# Example 3:
#
#
# Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
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

# @lc tags=binary-search;queue

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算不规则图形的面积。
# 计算所有面积，再减去连接在一起的面积。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        return sum((2 if grid[i][j] > 0 else 0) + 4 * grid[i][j] - 2 *
                   ((min(grid[i][j], grid[i][j + 1]) if j + 1 < n else 0) +
                    (min(grid[i][j], grid[i + 1][j]) if i + 1 < n else 0))
                   for i, j in product(range(n), range(n)))

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,2],[3,4]]')
    print('Exception :')
    print('34')
    print('Output :')
    print(str(Solution().surfaceArea([[1, 2], [3, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,1,1],[1,0,1],[1,1,1]]')
    print('Exception :')
    print('32')
    print('Output :')
    print(str(Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[2,2,2],[2,1,2],[2,2,2]]')
    print('Exception :')
    print('46')
    print('Output :')
    print(str(Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]])))
    print()

    pass
# @lc main=end