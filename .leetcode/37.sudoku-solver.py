#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (47.01%)
# Likes:    2678
# Dislikes: 104
# Total Accepted:    232.4K
# Total Submissions: 493.4K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
# of the grid.
#
#
# The '.' character indicates empty cells.
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output:
# [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is
# shown below:
#
#
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
#
#
#
#
#
# @lc idea=start
#
# 解数独，回溯。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.board = board
        self.init()
        self.do(0, 0)
        self.recover()
        return self.board

    def recover(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] =str(self.board[i][j])

    def do(self, i, j):
        if i == 9:
            return True
        if self.board[i][j] == 0:
            for n in range(1, 10):
                if self.r[i][n] and self.c[j][n] and self.b[i // 3 * 3 + j // 3][n]:
                    self.r[i][n] = False
                    self.c[j][n] = False
                    self.b[i // 3 * 3 + j // 3][n] = False
                    self.board[i][j] = n
                    if self.do((i + (j + 1) // 9), (j + 1) % 9):
                        return True
                    self.board[i][j] = 0
                    self.r[i][n] = True
                    self.c[j][n] = True
                    self.b[i // 3 * 3 + j // 3][n] = True

        else:
            return self.do((i + (j + 1) // 9), (j + 1) % 9)
        return False

    def init(self):
        self.r = [[True for _ in range(10)] for _ in range(9)]
        self.c = [[True for _ in range(10)] for _ in range(9)]
        self.b = [[True for _ in range(10)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = ord(self.board[i][j]) - 48
                    self.r[i][self.board[i][j]] = False
                    self.c[j][self.board[i][j]] = False
                    self.b[i // 3 * 3 + j // 3][self.board[i][j]] = False


# @lc code=end

if __name__ == '__main__':
    print(Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
        "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
