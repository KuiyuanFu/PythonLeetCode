# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
# https://leetcode.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (64.80%)
# Likes:    1816
# Dislikes: 37
# Total Accepted:    79.1K
# Total Submissions: 122.1K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# You are given an m x n binary matrix grid, where 0 represents a sea cell and
# 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent
# (4-directionally) land cell or walking off the boundary of the grid.
#
# Return the number of land cells in grid for which we cannot walk off the
# boundary of the grid in any number of moves.
#
#
# Example 1:
#
#
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is
# not enclosed because its on the boundary.
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
#
#
#

# @lc tags=array;dynamic-programming;sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定棋盘，0代表海洋，1代表陆地，求被海洋完全包围的陆地个数。
# 从边界向内遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        if m == 1 or n == 1:
            return 0
        res = 0
        q = []
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                res += 1
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    res -= 1
                    grid[i][j] = 0
                    q.append((i, j))
        ofs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            i, j = q.pop()
            for oi, oj in ofs:
                ni, nj = i + oi, j + oj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    res -= 1
                    q.append((ni, nj))
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0],
                                    [0, 0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(
        str(Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0],
                                    [0, 0, 0, 0]])))
    print()

    pass
# @lc main=end