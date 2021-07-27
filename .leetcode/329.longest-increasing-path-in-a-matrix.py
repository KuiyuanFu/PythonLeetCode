# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (47.35%)
# Likes:    3741
# Dislikes: 62
# Total Accepted:    245.6K
# Total Submissions: 518.6K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
#
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
#
#
# Example 1:
#
#
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
#
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
#
#
# Example 3:
#
#
# Input: matrix = [[1]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
#
#
#

# @lc tags=depth-first-search;topological-sort;memoization

# @lc imports=start
from heapq import heappop
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维棋盘，求最长的连续递增路径。
# 直接堆优先队列，贪心、动态规划计算长度。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        points = [(matrix[i][j], i, j) for i in range(rows)
                  for j in range(cols)]
        dp = [[1 for _ in range(cols)] for _ in range(rows)]
        from heapq import heapify
        heapify(points)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = 0
        while points:
            v, i, j = heappop(points)
            result = max(result, dp[i][j])
            for oi, oj in directions:
                ia, ja = i + oi, j + oj
                if 0 <= ia < rows and 0 <= ja < cols:
                    if matrix[ia][ja] > v:
                        dp[ia][ja] = max(dp[ia][ja], dp[i][j] + 1)

        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[9,9,4],[6,6,8],[2,1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1,
                                                                     1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[3,4,5],[3,2,6],[2,2,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2,
                                                                     1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('matrix = [[1]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().longestIncreasingPath([[1]])))
    print()

    pass
# @lc main=end