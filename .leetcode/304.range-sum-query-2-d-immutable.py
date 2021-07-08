# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (43.69%)
# Likes:    1855
# Dislikes: 220
# Total Accepted:    176.6K
# Total Submissions: 401.2K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
# '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, handle multiple queries of the following
# type:
#
#
# Calculate the sum of the elements of matrix inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).
#
#
# Implement the NumMatrix class:
#
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix
# matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the
# elements of matrix inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
#
#
#
# Example 1:
#
#
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
#
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green
# rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue
# rectangle)
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10^5 <= matrix[i][j] <= 10^5
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10^4 calls will be made to sumRegion.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维整数数组，求指定范围内的和。
# 将计算每一个位置的所有左上方的值，之后一个范围内的和，等于右下角加左上角，减左下角和右上角。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            n = 0
            for j in range(cols):
                n += matrix[i][j]
                self.matrix[i + 1][j + 1] = self.matrix[i][j + 1] + n

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2 + 1][col2 + 1] + self.matrix[row1][col1]\
               - self.matrix[row2 + 1][col1] - self.matrix[row1][col2 + 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end