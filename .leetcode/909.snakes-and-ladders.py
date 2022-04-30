# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#
# https://leetcode.com/problems/snakes-and-ladders/description/
#
# algorithms
# Medium (40.46%)
# Likes:    637
# Dislikes: 161
# Total Accepted:    73.7K
# Total Submissions: 181.9K
# Testcase Example:  '[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]'
#
# You are given an n x n integer matrix board where the cells are labeled from
# 1 to n^2 in a Boustrophedon style starting from the bottom left of the board
# (i.e. board[n - 1][0]) and alternating direction each row.
#
# You start on square 1 of the board. In each move, starting from square curr,
# do the following:
#
#
# Choose a destination square next with a label in the range [curr + 1,
# min(curr + 6, n^2)].
#
#
# This choice simulates the result of a standard 6-sided die roll: i.e., there
# are always at most 6 destinations, regardless of the size of the
# board.
#
#
# If next has a snake or ladder, you must move to the destination of that snake
# or ladder. Otherwise, you move to next.
# The game ends when you reach the square n^2.
#
#
# A board square on row r and column c has a snake or ladder if board[r][c] !=
# -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n^2
# do not have a snake or ladder.
#
# Note that you only take a snake or ladder at most once per move. If the
# destination to a snake or ladder is the start of another snake or ladder, you
# do not follow the subsequent snake or ladder.
#
#
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move,
# your destination square is 2. You follow the ladder to square 3, but do not
# follow the subsequent ladder to 4.
#
#
# Return the least number of moves required to reach the square n^2. If it is
# not possible to reach the square, return -1.
#
#
# Example 1:
#
#
# Input: board =
# [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so
# return 4.
#
#
# Example 2:
#
#
# Input: board = [[-1,-1],[-1,3]]
# Output: 1
#
#
#
# Constraints:
#
#
# n == board.length == board[i].length
# 2 <= n <= 20
# grid[i][j] is either -1 or in the range [1, n^2].
# The squares labeled 1 and n^2 do not have any ladders or snakes.
#
#
#

# @lc tags=math;dynamic-programming;minimax

# @lc imports=start
from tkinter import N, W
from imports import *

# @lc imports=end

# @lc idea=start
#
# 蛇形棋盘，从左下移动到右上，每一次移动加1-6步，其中有捷径，求最少移动次数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def getIdx(cur):
            row = cur // n
            col = cur % n
            if row % 2 == 1:
                col = n - 1 - col
            row = n - 1 - row
            return row, col

        length = n * n
        dp = [length] * length
        dp[0] = 0

        step = 0
        curs = set([0])
        while len(curs) > 0:
            step += 1
            cursn = set()
            for cur in curs:
                for nextIdx in range(cur + 1, min(length, cur + 7)):

                    row, col = getIdx(nextIdx)
                    b = board[row][col]
                    if b == -1:
                        if dp[nextIdx] > step:
                            dp[nextIdx] = step
                            cursn.add(nextIdx)
                    else:
                        if dp[b - 1] > step:
                            dp[b - 1] = step
                            cursn.add(b - 1)

            curs = cursn

        return dp[-1] if dp[-1] != length else -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1,
                                                                   1]])))

    print(
        str(Solution().snakesAndLadders([[-1, -1, -1, 46, 47, -1, -1, -1],
                                         [51, -1, -1, 63, -1, 31, 21, -1],
                                         [-1, -1, 26, -1, -1, 38, -1, -1],
                                         [-1, -1, 11, -1, 14, 23, 56, 57],
                                         [11, -1, -1, -1, 49, 36, -1, 48],
                                         [-1, -1, -1, 33, 56, -1, 57, 21],
                                         [-1, -1, -1, -1, -1, -1, 2, -1],
                                         [-1, -1, -1, 8, 3, -1, 6, 56]])))

    print(
        str(Solution().snakesAndLadders([[-1, -1, 2, -1], [14, 2, 12, 3],
                                         [4, 9, 1, 11], [-1, 2, 1, 16]])))

    print(
        str(Solution().snakesAndLadders([[-1, -1, 30, 14, 15, -1],
                                         [23, 9, -1, -1, -1, 9],
                                         [12, 5, 7, 24, -1, 30],
                                         [10, -1, -1, -1, 25, 17],
                                         [32, -1, 28, -1, -1, 32],
                                         [-1, -1, 23, -1, 13, 19]])))

    print(
        str(Solution().snakesAndLadders([[-1, 4, -1], [6, 2, 6], [-1, 3,
                                                                  -1]])))

    print('Example 1:')
    print('Input : ')
    print(
        'board =[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]'
    )
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().snakesAndLadders([[-1, -1, -1, -1, -1, -1],
                                         [-1, -1, -1, -1, -1, -1],
                                         [-1, -1, -1, -1, -1, -1],
                                         [-1, 35, -1, -1, 13, -1],
                                         [-1, -1, -1, -1, -1, -1],
                                         [-1, 15, -1, -1, -1, -1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [[-1,-1],[-1,3]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().snakesAndLadders([[-1, -1], [-1, 3]])))
    print()

    pass
# @lc main=end