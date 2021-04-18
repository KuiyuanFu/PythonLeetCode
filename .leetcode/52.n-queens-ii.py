# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (60.52%)
# Likes:    800
# Dislikes: 182
# Total Accepted:    159.6K
# Total Submissions: 263.2K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
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


# @lc tags=backtracking

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# n皇后问题，皇后不能在同一行、列、斜线。
# 直接回溯。比上一题要简化一点。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.b = n - 1
        self.flags = [[0 for _ in range(n)] for _ in range(n)]
        self.results = 0
        self.solveNQueensRecur(0)
        return self.results

    def solveNQueensRecur(self, r: int):
        if r == self.n:
            self.results+=1
            return

        for j, f in enumerate(self.flags[r]):
            if f == 0:
                self.setFlag(r, j, 1)
                self.solveNQueensRecur(r+1)
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


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Output :')
    print(str(Solution().totalNQueens(4)))
    print('Exception :')
    print('2')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().totalNQueens(1)))
    print('Exception :')
    print('1')
    print()
    
    pass
# @lc main=end