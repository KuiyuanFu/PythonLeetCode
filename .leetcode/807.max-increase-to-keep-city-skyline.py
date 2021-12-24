# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
#
# algorithms
# Medium (84.91%)
# Likes:    1493
# Dislikes: 387
# Total Accepted:    115.3K
# Total Submissions: 135.4K
# Testcase Example:  '[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]'
#
# There is a city composed of n x n blocks, where each block contains a single
# building shaped like a vertical square prism. You are given a 0-indexed n x n
# integer matrix grid where grid[r][c] represents the height of the building
# located in the block at row r and column c.
#
# A city's skyline is the the outer contour formed by all the building when
# viewing the side of the city from a distance. The skyline from each cardinal
# direction north, east, south, and west may be different.
#
# We are allowed to increase the height of any number of buildings by any
# amount (the amount can be different per building). The height of a 0-height
# building can also be increased. However, increasing the height of a building
# should not affect the city's skyline from any cardinal direction.
#
# Return the maximum total sum that the height of the buildings can be
# increased by without changing the city's skyline from any cardinal
# direction.
#
#
# Example 1:
#
#
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: The building heights are shown in the center of the above image.
# The skylines when viewed from each cardinal direction are drawn in red.
# The grid after increasing the height of buildings without affecting skylines
# is:
# gridNew = [ [8, 4, 8, 7],
# ⁠           [7, 4, 7, 7],
# ⁠           [9, 4, 8, 7],
# ⁠           [3, 3, 3, 3] ]
#
#
# Example 2:
#
#
# Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
# Output: 0
# Explanation: Increasing the height of any building will result in the skyline
# changing.
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[r].length
# 2 <= n <= 50
# 0 <= grid[r][c] <= 100
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 城市天际线，不改变天际线的条件下，楼最多可与增加多少层。
# 直接统计。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        colMs = [max(grid[i]) for i in range(n)]
        grid = list(zip(*grid))
        rowMs = [max(grid[i]) for i in range(n)]
        return sum((min(rowMs[i], colMs[j]) - grid[i][j])
                   for i, j in product(range(n), range(n)))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]')
    print('Exception :')
    print('35')
    print('Output :')
    print(
        str(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7],
                                                  [9, 2, 6, 3], [0, 3, 1,
                                                                 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,0,0],[0,0,0],[0,0,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(
        str(Solution().maxIncreaseKeepingSkyline([[0, 0, 0], [0, 0, 0],
                                                  [0, 0, 0]])))
    print()

    pass
# @lc main=end