# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (39.60%)
# Likes:    1275
# Dislikes: 175
# Total Accepted:    57.8K
# Total Submissions: 145.8K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m x n grid with a ball. The ball is initially at the position
# [startRow, startColumn]. You are allowed to move the ball to one of the four
# adjacent cells in the grid (possibly out of the grid crossing the grid
# boundary). You can apply at most maxMove moves to the ball.
#
# Given the five integers m, n, maxMove, startRow, startColumn, return the
# number of paths to move the ball out of the grid boundary. Since the answer
# can be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
#
#
# Example 2:
#
#
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n
#
#
#

# @lc tags=dynamic-programming;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 球提出边界的走法。
# 直接暴力。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int,
                  startColumn: int) -> int:

        d = {(startRow, startColumn): 1}
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        res = 0
        for _ in range(maxMove):
            dn = defaultdict(int)
            for k in d.keys():
                i, j = k
                times = d[k]
                for oi, oj in directions:
                    ni, nj = i + oi, j + oj
                    if 0 <= ni < m and 0 <= nj < n:
                        dn[(ni, nj)] += times
                    else:
                        res += times
            d = dn
        return res % 1000000007


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findPaths(2, 2, 2, 0, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().findPaths(1, 3, 3, 0, 1)))
    print()
    print(str(Solution().findPaths(8, 50, 23, 5, 26)))
    pass
# @lc main=end