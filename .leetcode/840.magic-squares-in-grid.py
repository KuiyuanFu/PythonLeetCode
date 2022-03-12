# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#
# https://leetcode.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Medium (38.33%)
# Likes:    242
# Dislikes: 1439
# Total Accepted:    31.7K
# Total Submissions: 82.6K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
#
# Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids
# are there?  (Each subgrid is contiguous).
#
#
# Example 1:
#
#
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
#
# while this one is not:
#
# In total, there is only one magic square inside the given grid.
#
#
# Example 2:
#
#
# Input: grid = [[8]]
# Output: 0
#
#
#
# Constraints:
#
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
#
#
#

# @lc tags=Unknown

# @lc imports=start
from inspect import formatargvalues
from nntplib import GroupInfo
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计二维数组中，任意3x3区域中，包含1-9，且行、列、斜线的和相等。
# 中心必须是5。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        if row < 3 or col < 3:

            return 0

        res = 0

        adjoins = [
            (0, -1, -1),
            (1, -1, 0),
            (2, -1, 1),
            (3, 0, 1),
            (4, 1, 1),
            (5, 1, 0),
            (6, 1, -1),
            (7, 0, -1),
        ]
        values = [4, 3, 8, 1, 6, 7, 2, 9, 4]
        keys = {4: 0, 8: 2, 6: 4, 2: 6}

        def valid(idx, i, j):
            f = True
            for oidx, oi, oj in adjoins:
                if grid[i + oi][j + oj] != values[(idx + oidx) % 8]:
                    f = False
                    break
            if f:
                return f
            for oidx, oi, oj in adjoins:
                if grid[i + oi][j + oj] != values[(idx - oidx + 8) % 8]:
                    return False
            return True

        res = 0

        for i, j in product(range(1, row - 1), range(1, col - 1)):
            if grid[i][j] != 5:
                continue
            if grid[i - 1][j - 1] not in keys:
                continue
            idx = keys[grid[i - 1][j - 1]]
            if valid(idx, i, j):
                res += 1

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().numMagicSquaresInside([[8, 3, 4], [1, 5, 9], [6, 7,
                                                                     2]])))
    print('Example 1:')
    print('Input : ')
    print('grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9],
                                              [2, 7, 6, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[8]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numMagicSquaresInside([[8]])))
    print(
        str(Solution().numMagicSquaresInside([[8, 1, 6], [3, 5, 7], [4, 9,
                                                                     2]])))
    print()

    pass
# @lc main=end