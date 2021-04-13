#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (50.14%)
# Likes:    2832
# Dislikes: 104
# Total Accepted:    249.5K
# Total Submissions: 496.6K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#
#
#
# @lc idea=start
#
# n皇后问题，皇后不能在同一行、列、斜线。
# 直接回溯。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.b = n - 1
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.flags = [[0 for _ in range(n)] for _ in range(n)]
        self.results = []
        self.solveNQueensRecur(0)
        return self.results

    def solveNQueensRecur(self, r: int):
        if r == self.n:
            self.results.append([''.join(l) for l in self.board])
            return

        for j, f in enumerate(self.flags[r]):
            if f == 0:
                self.board[r][j] = 'Q'
                self.setFlag(r, j, 1)
                self.solveNQueensRecur(r+1)
                self.board[r][j] = '.'
                self.setFlag(r, j, -1)

    def setFlag(self, iS, jS, flag):
        i, j = iS, jS
        while i < self.b and j >0:
            i += 1
            j -= 1
            self.flags[i][j] += flag
        i, j = iS, jS
        while i < self.b and j < self.b:
            i += 1
            j += 1
            self.flags[i][j] += flag
        i, j = iS, jS
        while i < self.b:
            i += 1
            self.flags[i][j] += flag


# @lc code=end
if __name__ == '__main__':
    print(Solution().solveNQueens(1))
    print(Solution().solveNQueens(2))
    print(Solution().solveNQueens(3))
    print(Solution().solveNQueens(4))
