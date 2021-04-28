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

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维矩阵，按照顺时针旋转顺序输出矩阵的所有元素。
# 那就旋转，之后按行输出。
# 使用zip 实现，每一次输出第一行后，将剩余矩阵顺时针旋转，这样就将最右侧的一列，变成了第一行。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) != 0:
            result = result + list(matrix[0])
            # zip(*) 是将输入的每一行视为单独的输入，之后讲每一列组成新的元组，作为新的一行。
            matrix = list(zip(*matrix[1:]))[::-1]
        return result

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Output :')
    print(str(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    print('Exception :')
    print('[1,2,3,6,9,8,7,4,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]')
    print('Output :')
    print(
        str(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8],
                                    [9, 10, 11, 12]])))
    print('Exception :')
    print('[1,2,3,4,8,12,11,10,9,5,6,7]')
    print()

    pass
# @lc main=end