# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#
# https://leetcode.com/problems/battleships-in-a-board/description/
#
# algorithms
# Medium (72.09%)
# Likes:    1098
# Dislikes: 660
# Total Accepted:    123.8K
# Total Submissions: 171.7K
# Testcase Example:  '[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]'
#
# Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
# return the number of the battleships on board.
#
# Battleships can only be placed horizontally or vertically on board. In other
# words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1
# (k rows, 1 column), where k can be of any size. At least one horizontal or
# vertical cell separates between two battleships (i.e., there are no adjacent
# battleships).
#
#
# Example 1:
#
#
# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
#
#
# Example 2:
#
#
# Input: board = [["."]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is either '.' or 'X'.
#
#
#
# Follow up: Could you do it in one-pass, using only O(1) extra memory and
# without modifying the values board?
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算二维数组中有多少个块。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        res = 0
        for i, j in product(range(rows), range(cols)):
            if board[i][j] == '.':
                continue
            if i > 0 and board[i - 1][j] == 'X':
                continue
            if j > 0 and board[i][j - 1] == 'X':
                continue
            res += 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().countBattleships([["X", ".", ".", "X"],
                                         [".", ".", ".", "X"],
                                         [".", ".", ".", "X"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [["."]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countBattleships([["."]])))
    print()

    pass
# @lc main=end