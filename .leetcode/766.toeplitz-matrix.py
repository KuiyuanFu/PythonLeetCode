# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#
# https://leetcode.com/problems/toeplitz-matrix/description/
#
# algorithms
# Easy (66.25%)
# Likes:    1658
# Dislikes: 110
# Total Accepted:    153.2K
# Total Submissions: 229.3K
# Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'
#
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
# return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
# same elements.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
#
#
# Example 2:
#
#
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
#
#
#
# Follow up:
#
#
# What if the matrix is stored on disk, and the memory is limited such that you
# can only load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into
# the memory at once?
#
#
#

# @lc tags=linked-list;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 每条左上到右下的斜线都是同一元素。
# 直接判断，不在最下与最右的，每个元素的右下角元素是否与其相等。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        for i, j in product(range(rows - 1), range(cols - 1)):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3],
                                         [9, 5, 1, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,2],[2,2]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isToeplitzMatrix([[1, 2], [2, 2]])))
    print()

    pass
# @lc main=end