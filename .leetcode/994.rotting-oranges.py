# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (52.35%)
# Likes:    8384
# Dislikes: 307
# Total Accepted:    487K
# Total Submissions: 930.3K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 感染，每次一格，问是否可以全部感染，若可以返回时间
# 直接遍历
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        q = []
        freshCount = 0
        for i, j in product(range(m), range(n)):
            g = grid[i][j]
            if g == 2:
                q.append((i, j))
            elif g == 1:
                freshCount += 1
        if freshCount == 0:
            return 0
        res = -1
        while q:
            qn = []
            for i, j in q:
                for oi, oj in offsets:
                    ni, nj = i + oi, j + oj
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            freshCount -= 1
                            grid[ni][nj] = 2
                            qn.append((ni, nj))
            q = qn
            res += 1
        if freshCount == 0:
            return res
        else:
            return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[2,1,1],[1,1,0],[0,1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[2,1,1],[0,1,1],[1,0,1]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[0,2]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().orangesRotting([[0, 2]])))
    print()

    pass
# @lc main=end