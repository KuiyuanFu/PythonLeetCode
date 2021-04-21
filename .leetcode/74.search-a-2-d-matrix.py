# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (38.20%)
# Likes:    3155
# Dislikes: 195
# Total Accepted:    440.6K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

# @lc tags=array;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在二维矩阵中有效查找一个元素，这个矩阵满足，每一行是有序的，每行的第一个元素大于上一行的最后一个元素。
# 二分搜索，将线性索引转化为矩阵上的索引。
#
# @lc idea=end

# @lc group=binary-search

# @lc rank=5


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m // cols][m % cols] == target:
                return True
            elif matrix[m // cols][m % cols] < target:
                l = m + 1
            else:
                r = m - 1

        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3')
    print('Output :')
    print(
        str(Solution().searchMatrix(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13')
    print('Output :')
    print(
        str(Solution().searchMatrix(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end