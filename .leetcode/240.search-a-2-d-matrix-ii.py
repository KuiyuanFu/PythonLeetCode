# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (45.70%)
# Likes:    4991
# Dislikes: 94
# Total Accepted:    465.5K
# Total Submissions: 1M
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
# '5'
#
# Write an efficient algorithm that searches for a target value in an m x n
# integer matrix. The matrix has the following properties:
#
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
#
# Example 1:
#
#
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
#
#
# Example 2:
#
#
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
#
#
#

# @lc tags=binary-search;divide-and-conquer

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在一个二维数组中，查找元素，数组满足左上小于右下。
# 直接二分搜索。得到中值后，判断是否等于，若不等于，则三次递归。若小于，则将此空间分为四份，右侧，右下，下方。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rSearchMatrix(xl, yl, xu, yu):
            if xl <= xu and yl <= yu:
                xm, ym = (xl + xu) // 2, (yl + yu) // 2
                if matrix[xm][ym] == target:
                    return True
                elif matrix[xm][ym] < target:
                    # right
                    r1 = rSearchMatrix(xm + 1, yl, xu, ym)
                    # dwon
                    r2 = rSearchMatrix(xl, ym + 1, xm, yu)
                    # right dowm
                    r3 = rSearchMatrix(xm + 1, ym + 1, xu, yu)
                    return r1 or r2 or r3
                else:
                    #  up
                    r1 = rSearchMatrix(xl, ym, xm - 1, yu)
                    # left
                    r2 = rSearchMatrix(xm, yl, xu, ym - 1)
                    # left up
                    r3 = rSearchMatrix(xl, yl, xm - 1, ym - 1)
                    return r1 or r2 or r3

            return False

        return rSearchMatrix(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().searchMatrix(
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 15)))
    print('Example 1:')
    print('Input : ')
    print(
        'matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target = 5'
    )
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],target = 20'
    )
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)))
    print()

    pass
# @lc main=end