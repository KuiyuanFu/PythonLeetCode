# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#
# https://leetcode.com/problems/cherry-pickup/description/
#
# algorithms
# Hard (35.71%)
# Likes:    2131
# Dislikes: 111
# Total Accepted:    46K
# Total Submissions: 128.1K
# Testcase Example:  '[[0,1,-1],[1,0,-1],[1,1,1]]'
#
# You are given an n x n grid representing a field of cherries, each cell is
# one of three possible integers.
#
#
# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through,
# or
# -1 means the cell contains a thorn that blocks your way.
#
#
# Return the maximum number of cherries you can collect by following the rules
# below:
#
#
# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right
# or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up
# through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the
# cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries
# can be collected.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right right to
# reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes
# [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more
# cherry.
# The total number of cherries picked up is 5, and this is the maximum
# possible.
#
#
# Example 2:
#
#
# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# grid[i][j] is -1, 0, or 1.
# grid[0][0] != -1
# grid[n - 1][n - 1] != -1
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from sys import getprofile
from imports import *

# @lc imports=end

# @lc idea=start
#
# 左上到右下，往返移动一次，最多收集多少水果。
# dp。
# 使用四元组(i,j,p,q)表示到(i,j)与(p,q)两点时，最多的水果个数，满足n=i+j=p+q，使用(n,i,p)三元组简化表示，并使用(i,p)两元组再次简化。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = (N << 1) - 1
        if grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[0][0] = grid[0][0]

        for n in range(1, M):
            for i in reversed(range(N)):
                for p in reversed(range(N)):
                    j = n - i
                    q = n - p
                    if not 0 <= j < N or not 0 <= q < N or grid[i][
                            j] < 0 or grid[p][q] < 0:
                        dp[i][p] = -1
                        continue
                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i - 1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p - 1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])
                    if dp[i][p] >= 0:
                        dp[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)

        return max(0, dp[-1][-1])


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().cherryPickup([[0, 1, 1, 0, 0], [1, 1, 1, 1, 0],
                                     [-1, 1, 1, 1, -1], [0, 1, 1, 1, 0],
                                     [1, 0, -1, 0, 0]])))

    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1,-1],[1,0,-1],[1,1,1]]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,1,-1],[1,-1,1],[-1,1,1]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().cherryPickup([[1, 1, -1], [1, -1, 1], [-1, 1, 1]])))
    print()

    pass
# @lc main=end