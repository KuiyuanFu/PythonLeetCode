# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (61.15%)
# Likes:    1109
# Dislikes: 370
# Total Accepted:    128.9K
# Total Submissions: 210.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
#
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 翻转
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Exception :')
    print('[[1,4,7],[2,5,8],[3,6,9]]')
    print('Output :')
    print(str(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,2,3],[4,5,6]]')
    print('Exception :')
    print('[[1,4],[2,5],[3,6]]')
    print('Output :')
    print(str(Solution().transpose([[1, 2, 3], [4, 5, 6]])))
    print()

    pass
# @lc main=end