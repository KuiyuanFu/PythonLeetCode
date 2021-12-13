# @lc app=leetcode id=803 lang=python3
#
# [803] Bricks Falling When Hit
#
# https://leetcode.com/problems/bricks-falling-when-hit/description/
#
# algorithms
# Hard (32.77%)
# Likes:    708
# Dislikes: 163
# Total Accepted:    22.6K
# Total Submissions: 67.7K
# Testcase Example:  '[[1,0,0,0],[1,1,1,0]]\n[[1,0]]'
#
# You are given an m x n binary grid, where each 1 represents a brick and 0
# represents an empty space. A brick is stable if:
#
#
# It is directly connected to the top of the grid, or
# At least one other brick in its four adjacent cells is stable.
#
#
# You are also given an array hits, which is a sequence of erasures we want to
# apply. Each time we want to erase the brick at the location hits[i] = (rowi,
# coli). The brick on that location (if it exists) will disappear. Some other
# bricks may no longer be stable because of that erasure and will fall. Once a
# brick falls, it is immediately erased from the grid (i.e., it does not land
# on other stable bricks).
#
# Return an array result, where each result[i] is the number of bricks that
# will fall after the i^th erasure is applied.
#
# Note that an erasure may refer to a location with no brick, and if it does,
# no bricks drop.
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# Explanation: Starting with the grid:
# [[1,0,0,0],
# ⁠[1,1,1,0]]
# We erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
# ⁠[0,1,1,0]]
# The two underlined bricks are no longer stable as they are no longer
# connected to the top nor adjacent to another stable brick, so they will fall.
# The resulting grid is:
# [[1,0,0,0],
# ⁠[0,0,0,0]]
# Hence the result is [2].
#
#
# Example 2:
#
#
# Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# Output: [0,0]
# Explanation: Starting with the grid:
# [[1,0,0,0],
# ⁠[1,1,0,0]]
# We erase the underlined brick at (1,1), resulting in the grid:
# [[1,0,0,0],
# ⁠[1,0,0,0]]
# All remaining bricks are still stable, so no bricks fall. The grid remains
# the same:
# [[1,0,0,0],
# ⁠[1,0,0,0]]
# Next, we erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
# ⁠[0,0,0,0]]
# Once again, all remaining bricks are still stable, so no bricks fall.
# Hence the result is [0,0].
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is 0 or 1.
# 1 <= hits.length <= 4 * 10^4
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# All (xi, yi) are unique.
#
#
#

# @lc tags=dynamic-programming;heap;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 消除方块，问每消除一个后，有多少个随之掉落。
# 反向操作，倒序，计算每添加一个，有多少个可以添加。
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:
    def hitBricks(self, grid: List[List[int]],
                  hits: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        for i, j in hits:
            if grid[i][j] == 1:
                grid[i][j] = 2
        hits.reverse()
        res = []

        def traverse(s: List) -> int:
            r = 0
            while s:
                i, j = s.pop()
                if not (0 <= i < rows and 0 <= j < cols):
                    continue
                if grid[i][j] == 2:
                    grid[i][j] = 3
                if grid[i][j] != 1:
                    continue
                grid[i][j] = 4
                s.append((i + 1, j))
                s.append((i, j + 1))
                s.append((i - 1, j))
                s.append((i, j - 1))
                r += 1
            return r - 1 if r > 0 else 0

        traverse([(0, j) for j in range(cols)])
        for i, j in hits:
            ls = []
            if grid[i][j] == 3:
                ls.append((i, j))
            if grid[i][j] == 2 or grid[i][j] == 3:
                grid[i][j] = 1
            res.append(traverse(ls))
        res.reverse()
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]')
    print('Exception :')
    print('[0,0]')
    print('Output :')
    print(
        str(Solution().hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]],
                                 [[1, 1], [1, 0]])))
    print()
    print('Example 2:')
    print('Input : ')
    print(
        'grid = [[1],[1],[1],[1],[1]], hits =[[3,0],[4,0],[1,0],[2,0],[0,0]]')
    print('Exception :')
    print('[1,0,1,0,0]')
    print('Output :')
    print(
        str(Solution().hitBricks([[1], [1], [1], [1], [1]],
                                 [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]])))
    print()

    pass
# @lc main=end