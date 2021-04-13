#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (36.44%)
# Likes:    3691
# Dislikes: 656
# Total Accepted:    485.8K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#
#
#
# @lc idea=start
#
# 按照旋转顺序输出矩阵的所有元素。
# 那就旋转，之后按行输出，使用zip 实现。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) != 0:
            result = result + list(matrix[0])
            matrix = list(zip(*matrix[1:]))[::-1]
        return result

# @lc code=end


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution().spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
