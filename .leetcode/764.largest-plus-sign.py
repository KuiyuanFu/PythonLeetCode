# @lc app=leetcode id=764 lang=python3
#
# [764] Largest Plus Sign
#
# https://leetcode.com/problems/largest-plus-sign/description/
#
# algorithms
# Medium (47.22%)
# Likes:    987
# Dislikes: 182
# Total Accepted:    45.7K
# Total Submissions: 94.2K
# Testcase Example:  '5\n[[4,2]]'
#
# You are given an integer n. You have an n x n binary grid grid with all
# values initially 1's except for some indices given in the array mines. The
# i^th element of the array mines is defined as mines[i] = [xi, yi] where
# grid[xi][yi] == 0.
#
# Return the order of the largest axis-aligned plus sign of 1's contained in
# grid. If there is none, return 0.
#
# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1
# along with four arms of length k - 1 going up, down, left, and right, and
# made of 1's. Note that there could be 0's or 1's beyond the arms of the plus
# sign, only the relevant area of the plus sign is checked for 1's.
#
#
# Example 1:
#
#
# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2.
# One of them is shown.
#
#
# Example 2:
#
#
# Input: n = 1, mines = [[0,0]]
# Output: 0
# Explanation: There is no plus sign, so return 0.
#
#
#
# Constraints:
#
#
# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# All the pairs (xi, yi) are unique.
#
#
#

# @lc tags=tree;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找最大的全1加号。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n for _ in range(n)] for _ in range(n)]
        for i, j in mines:
            grid[i][j] = 0

        for i in range(n):
            l, r, u, d = 0, 0, 0, 0
            for j in range(n):
                k = n - 1 - j

                l = 0 if grid[i][j] == 0 else (l + 1)
                grid[i][j] = min(grid[i][j], l)
                r = 0 if grid[i][k] == 0 else (r + 1)
                grid[i][k] = min(grid[i][k], r)
                u = 0 if grid[j][i] == 0 else (u + 1)
                grid[j][i] = min(grid[j][i], u)
                d = 0 if grid[k][i] == 0 else (d + 1)
                grid[k][i] = min(grid[k][i], d)
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, grid[i][j])

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5, mines = [[4,2]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().orderOfLargestPlusSign(5, [[4, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, mines = [[0,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().orderOfLargestPlusSign(1, [[0, 0]])))
    print()

    pass
# @lc main=end