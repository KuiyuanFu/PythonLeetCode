# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (67.54%)
# Likes:    2411
# Dislikes: 94
# Total Accepted:    130.5K
# Total Submissions: 192.9K
# Testcase Example:  '[[2,1,3],[6,5,4],[7,8,9]]'
#
# Given an n x n array of integers matrix, return the minimum sum of any
# falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element
# in the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col
# - 1), (row + 1, col), or (row + 1, col + 1).
#
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
#
#
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc tags=hash-table;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最小下落路径
# 动态规划
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        for row in range(1, n):
            rowPre = row - 1
            for col in range(n):
                colPres = [col]
                if col > 0:
                    colPres.append(col - 1)
                if col < n - 1:
                    colPres.append(col + 1)
                matrix[row][col] += min(matrix[rowPre][colPre]
                                        for colPre in colPres)
        return min(matrix[-1])
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[2,1,3],[6,5,4],[7,8,9]]')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[-19,57],[-40,-5]]')
    print('Exception :')
    print('-59')
    print('Output :')
    print(str(Solution().minFallingPathSum([[-19, 57], [-40, -5]])))
    print()

    pass
# @lc main=end