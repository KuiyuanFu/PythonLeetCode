# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (52.35%)
# Likes:    1558
# Dislikes: 443
# Total Accepted:    145.4K
# Total Submissions: 276.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix mat, return an array of all the elements of the array
# in a diagonal order.
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
#
#
# Example 2:
#
#
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
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
# -10^5 <= mat[i][j] <= 10^5
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 对角线遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = [0] * (rows * cols)

        i, j = 0, 0
        f = True
        for k in range(rows * cols):
            res[k] = mat[i][j]
            if f:
                i -= 1
                j += 1
                if j == cols:
                    i += 2
                    j -= 1
                    f = not f
                elif i < 0:
                    i += 1
                    f = not f

            else:
                i += 1
                j -= 1
                if i >= rows:
                    j += 2
                    i -= 1
                    f = not f
                elif j < 0:
                    j += 1
                    f = not f
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('mat = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Exception :')
    print('[1,2,4,7,5,3,6,8,9]')
    print('Output :')
    print(str(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('mat = [[1,2],[3,4]]')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().findDiagonalOrder([[1, 2], [3, 4]])))
    print()

    pass
# @lc main=end