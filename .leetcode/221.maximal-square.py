# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (40.02%)
# Likes:    4801
# Dislikes: 114
# Total Accepted:    369K
# Total Submissions: 917.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
#
# Example 1:
#
#
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
#
#
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
#
# Example 3:
#
#
# Input: matrix = [["0"]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 棋盘，求最大的矩形。
# 按行遍历，之后山峰迭代。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        for i in range(rows):
            matrix[i].append('0')
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = 0 if matrix[i][j] == '0' else 1
        for i in range(1, rows):
            for j in range(cols):
                matrix[i][j] = 0 if matrix[i][j] == 0 else matrix[i - 1][j] + 1
        ret = 0
        for i in range(rows):
            # j height
            dp = []
            for j in range(cols):
                mj = j
                height = matrix[i][j]
                while dp and dp[-1][1] >= height:
                    mj, mh = dp.pop()
                    ret = max(ret, min(mh, (j - mj))**2)
                if dp and dp[-1][1] == height:
                    continue
                dp.append((mj, height))

        return ret
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().maximalSquare([["1", "0", "1",
                                       "0"], ["1", "0", "1", "1"],
                                      ["1", "0", "1", "1"],
                                      ["1", "1", "1", "1"]])))
    print('Example 1:')
    print('Input : ')
    print(
        'matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
    )
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().maximalSquare([["1", "0", "1", "0", "0"],
                                      ["1", "0", "1", "1", "1"],
                                      ["1", "1", "1", "1", "1"],
                                      ["1", "0", "0", "1", "0"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [["0","1"],["1","0"]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maximalSquare([["0", "1"], ["1", "0"]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('matrix = [["0"]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maximalSquare([["0"]])))
    print()

    pass
# @lc main=end