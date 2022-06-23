# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (52.94%)
# Likes:    2749
# Dislikes: 132
# Total Accepted:    98K
# Total Submissions: 184.4K
# Testcase Example:  '[[0,1],[1,0]]'
#
# You are given an n x n binary matrix grid where 1 represents land and 0
# represents water.
#
# An island is a 4-directionally connected group of 1's not connected to any
# other 1's. There are exactly two islands in grid.
#
# You may change 0's to 1's to connect the two islands to form one island.
#
# Return the smallest number of 0's you must flip to connect the two
# islands.
#
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
#
#
# Example 3:
#
#
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
#
#
#

# @lc tags=dynamic-programming;bit-manipulation

# @lc imports=start
from unittest import IsolatedAsyncioTestCase
from imports import *

# @lc imports=end

# @lc idea=start
#
# 两个岛相连，最短路径。
# 直接遍历
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # first island
        i, j = None, None
        for i, j in product(range(n), range(n)):
            if grid[i][j] == 1:
                break

        # neighborhoods
        edges = []
        islands = [(i, j)]
        while islands:
            i, j = islands.pop()
            if grid[i][j] == 1:
                for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= ni < n and 0 <= nj < n:
                        islands.append((ni, nj))
            elif grid[i][j] == 0:
                edges.append((i, j))
            grid[i][j] = 2

        # traversal
        res = 0
        while True:
            res += 1
            edgesNew = []
            for t in edges:
                i, j = t
                for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return res
                        elif grid[ni][nj] == 0:
                            edgesNew.append((ni, nj))
                            grid[ni][nj] = 2
            edges = edgesNew
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1],[1,0]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().shortestBridge([[0, 1], [1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0,1,0],[0,0,0],[0,0,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1],
                                       [1, 0, 1, 0, 1], [1, 0, 0, 0, 1],
                                       [1, 1, 1, 1, 1]])))
    print()

    pass
# @lc main=end