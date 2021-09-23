# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (42.93%)
# Likes:    3274
# Dislikes: 158
# Total Accepted:    169.2K
# Total Submissions: 393.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
#
# Example 1:
#
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
#
# Example 2:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
#
#
#

# @lc tags=depth-first-search;breadth-first-search

# @lc imports=start
from random import vonmisesvariate
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求最近的0的距离。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(mat), len(mat[0])
        rc = rows * cols
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = rc
        while q:
            i, j = q.popleft()
            vij = mat[i][j]
            if vij < 0:
                continue
            for oi, oj in directions:
                ni, nj = i + oi, j + oj
                if 0 <= ni < rows and 0 <= nj < cols:
                    vninj = mat[ni][nj]
                    if vninj > vij:
                        mat[ni][nj] = min(vninj, vij + 1)
                        q.append((ni, nj))
            mat[i][j] = -vij
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = -mat[i][j]
        return mat


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat = [[0,0,0],[0,1,0],[0,0,0]]')
    print('Exception :')
    print('[[0,0,0],[0,1,0],[0,0,0]]')
    print('Output :')
    print(str(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('mat = [[0,0,0],[0,1,0],[1,1,1]]')
    print('Exception :')
    print('[[0,0,0],[0,1,0],[1,2,1]]')
    print('Output :')
    print(str(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])))
    print()

    pass
# @lc main=end