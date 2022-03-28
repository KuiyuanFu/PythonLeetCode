# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#
# https://leetcode.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (74.71%)
# Likes:    1011
# Dislikes: 161
# Total Accepted:    33.9K
# Total Submissions: 45.3K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# You are given an m x n binary matrix grid.
#
# A move consists of choosing any row or column and toggling each value in that
# row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
#
# Every row of the matrix is interpreted as a binary number, and the score of
# the matrix is the sum of these numbers.
#
# Return the highest possible score after making any number of moves (including
# zero moves).
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
# Example 2:
#
#
# Input: grid = [[0]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid[i][j] is either 0 or 1.
#
#
#

# @lc tags=array

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 翻转，统计分数
# 每一行就是一个分数，每次翻转一行或一列
# 要使分数最大，将每一列当作一个数，第一列可以全一，之后每一行就不可换，只可以换每一列，使类一列的和最大。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        for i in range(row):
            if grid[i][0] == 0:
                for j in range(col):
                    grid[i][j] = 1 - grid[i][j]
        res = row
        for j in range(1, col):
            c1 = [grid[i][j] for i in range(row)].count(1)
            c1 = max(c1, row - c1)
            res = res * 2 + c1
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]')
    print('Exception :')
    print('39')
    print('Output :')
    print(
        str(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0,
                                                                 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[0]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().matrixScore([[0]])))
    print()

    pass
# @lc main=end