# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (79.58%)
# Likes:    3288
# Dislikes: 143
# Total Accepted:    126.3K
# Total Submissions: 158.7K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# You are given an m x n integer array grid where grid[i][j] could be:
#
#
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
#
#
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
#
# Example 2:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#
# Example 3:
#
#
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly
# once.
# Note that the starting and ending square can be anywhere in the grid.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# 1 <= m * n <= 20
# -1 <= grid[i][j] <= 2
# There is exactly one starting cell and one ending cell.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从开始位置到结束位置，遍历所有位置，求一共有多少种方式。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        target = 0
        q = []
        for i, j in product(range(rows), range(cols)):
            n = grid[i][j]
            if n == 0:
                target += 1
            elif n == 1:
                q.append([i, j, 0])
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        now = 0
        while q:
            i, j, d = q[-1]
            if d == 4:
                q.pop()
                now -= 1
                grid[i][j] = 0
            else:
                q[-1][2] = d + 1
                offset = offsets[d]
                ni, nj = i + offset[0], j + offset[1]
                if 0 <= ni < rows and 0 <= nj < cols:
                    n = grid[ni][nj]
                    if n == 0:
                        grid[ni][nj] = -2
                        q.append([ni, nj, 0])
                        now += 1
                    elif n == 2:
                        if now == target:
                            res += 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0],
                                       [0, 0, 2, -1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0],
                                       [0, 0, 0, 2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[0,1],[2,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().uniquePathsIII([[0, 1], [2, 0]])))
    print()

    pass
# @lc main=end