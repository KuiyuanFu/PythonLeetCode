# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (50.96%)
# Likes:    1631
# Dislikes: 260
# Total Accepted:    70.3K
# Total Submissions: 137.8K
# Testcase Example:  '3\n2\n0\n0'
#
# On an n x n chessboard, a knight starts at the cell (row, column) and
# attempts to make exactly k moves. The rows and columns are 0-indexed, so the
# top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
#
# A chess knight has eight possible moves it can make, as illustrated below.
# Each move is two cells in a cardinal direction, then one cell in an
# orthogonal direction.
#
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
#
# The knight continues moving until it has made exactly k moves or has moved
# off the chessboard.
#
# Return the probability that the knight remains on the board after it has
# stopped moving.
#
#
# Example 1:
#
#
# Input: n = 3, k = 2, row = 0, column = 0
# Output: 0.06250
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
# on the board.
# From each of those positions, there are also two moves that will keep the
# knight on the board.
# The total probability the knight stays on the board is 0.0625.
#
#
# Example 2:
#
#
# Input: n = 1, k = 0, row = 0, column = 0
# Output: 1.00000
#
#
#
# Constraints:
#
#
# 1 <= n <= 25
# 0 <= k <= 100
# 0 <= row, column <= n
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在棋盘上放置一个棋子，以马的行动方式。求马走确定步数后，还在棋盘上的概率。
# dp
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int,
                          column: int) -> float:
        if k == 0:
            return 1

        dp = [[1.0 for _ in range(n)] for _ in range(n)]
        dpn = [[1.0 for _ in range(n)] for _ in range(n)]
        direcs = [[1, -2], [2, -1], [-1, 2], [-2, 1], [1, 2], [2, 1], [-1, -2],
                  [-2, -1]]
        for _ in range(k):

            for i in range(n):
                for j in range(n):
                    t = 0
                    for oi, oj in direcs:
                        ni, nj = i + oi, j + oj
                        if 0 <= ni < n and 0 <= nj < n:
                            t += dp[ni][nj]
                    dpn[i][j] = t / 8

            dp, dpn = dpn, dp

        return dp[row][column]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, k = 2, row = 0, column = 0')
    print('Exception :')
    print('0.06250')
    print('Output :')
    print(str(Solution().knightProbability(3, 2, 0, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, k = 0, row = 0, column = 0')
    print('Exception :')
    print('1.00000')
    print('Output :')
    print(str(Solution().knightProbability(1, 0, 0, 0)))
    print()

    pass
# @lc main=end