# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (59.40%)
# Likes:    2871
# Dislikes: 356
# Total Accepted:    248K
# Total Submissions: 414.5K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
#
# The board is made up of an m x n grid of cells, where each cell has an
# initial state: live (represented by a 1) or dead (represented by a 0). Each
# cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia
# article):
#
#
# Any live cell with fewer than two live neighbors dies as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
#
#
# The next state is created by applying the above rules simultaneously to every
# cell in the current state, where births and deaths occur simultaneously.
# Given the current state of the m x n grid board, return the next state.
#
#
# Example 1:
#
#
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#
#
# Example 2:
#
#
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
#
#
#
# Follow up:
#
#
# Could you solve it in-place? Remember that the board needs to be updated
# simultaneously: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# upon the border of the array (i.e., live cells reach the border). How would
# you address these problems?
#
#
#

# @lc tags=array

# @lc imports=start
from sys import builtin_module_names
from imports import *

# @lc imports=end

# @lc idea=start
#
# 生命游戏，给定二维棋盘，每一个单元格为一个细胞，值为1或0，即生或死。
# 活着的细胞只有相邻8个细胞中存在2-3个活细胞时，继续存活。
# 死细胞在有3个活细胞时复活。
# 求下一个状态。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                n = 0
                for oi, oj in neighbors:
                    ni = i + oi
                    nj = j + oj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if board[ni][nj] & 1 == 1:
                            n += 1
                if n == 3 or (n == 2 and (board[i][j] & 1) == 1):
                    board[i][j] = board[i][j] | 2
        for i in range(rows):
            for j in range(cols):
                board[i][j] = board[i][j] >> 1
        return board


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]')
    print('Exception :')
    print('[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]')
    print('Output :')
    print(
        str(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0,
                                                                     0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [[1,1],[1,0]]')
    print('Exception :')
    print('[[1,1],[1,1]]')
    print('Output :')
    print(str(Solution().gameOfLife([[1, 1], [1, 0]])))
    print()

    pass
# @lc main=end