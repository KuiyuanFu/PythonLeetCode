# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
# https://leetcode.com/problems/reshape-the-matrix/description/
#
# algorithms
# Easy (61.96%)
# Likes:    1438
# Dislikes: 157
# Total Accepted:    157.7K
# Total Submissions: 254.2K
# Testcase Example:  '[[1,2],[3,4]]\n1\n4'
#
# In MATLAB, there is a handy function called reshape which can reshape an m x
# n matrix into a new one with a different size r x c keeping its original
# data.
#
# You are given an m x n matrix mat and two integers r and c representing the
# number of rows and the number of columns of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original
# matrix in the same row-traversing order as they were.
#
# If the reshape operation with given parameters is possible and legal, output
# the new reshaped matrix; Otherwise, output the original matrix.
#
#
# Example 1:
#
#
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
#
#
# Example 2:
#
#
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# resharp
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int,
                      c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c:
            return mat
        res = [[None for _ in range(c)] for _ in range(r)]
        n = r * c
        for i in range(n):
            res[i // c][i % c] = mat[i // cols][i % cols]
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat = [[1,2],[3,4]], r = 1, c = 4')
    print('Exception :')
    print('[[1,2,3,4]]')
    print('Output :')
    print(str(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('mat = [[1,2],[3,4]], r = 2, c = 4')
    print('Exception :')
    print('[[1,2],[3,4]]')
    print('Output :')
    print(str(Solution().matrixReshape([[1, 2], [3, 4]], 2, 4)))
    print()

    pass
# @lc main=end