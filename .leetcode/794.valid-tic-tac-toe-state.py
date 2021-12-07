# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (34.68%)
# Likes:    357
# Dislikes: 892
# Total Accepted:    41K
# Total Submissions: 117.2K
# Testcase Example:  '["O  ","   ","   "]'
#
# Given a Tic-Tac-Toe board as a string array board, return true if and only if
# it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
#
# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The
# ' ' character represents an empty square.
#
# Here are the rules of Tic-Tac-Toe:
#
#
# Players take turns placing characters into empty squares ' '.
# The first player always places 'X' characters, while the second player always
# places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never filled
# ones.
# The game ends when there are three of the same (non-empty) character filling
# any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
#
#
#
# Example 1:
#
#
# Input: board = ["O  ","   ","   "]
# Output: false
# Explanation: The first player always plays "X".
#
#
# Example 2:
#
#
# Input: board = ["XOX"," X ","   "]
# Output: false
# Explanation: Players take turns making moves.
#
#
# Example 3:
#
#
# Input: board = ["XXX","   ","OOO"]
# Output: false
#
#
# Example 4:
#
#
# Input: board = ["XOX","O O","XOX"]
# Output: true
#
#
#
# Constraints:
#
#
# board.length == 3
# board[i].length == 3
# board[i][j] is either 'X', 'O', or ' '.
#
#
#

# @lc tags=binary-search;heap;depth-first-search;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个九宫格是否合法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def count(c: str):
            return sum(l.count(c) for l in board)

        no, nx = count('O'), count('X')

        def win(c: str):
            ls = [l for l in board] + [''.join(l) for l in zip(*board)] + [
                ''.join([board[i][i] for i in range(3)]),
                ''.join([board[2 - i][i] for i in range(3)]),
            ]
            t = c * 3
            return t in ls

        wo, wx = win('O'), win('X')
        if wo and wx:
            return False
        if wx and nx != no + 1:
            return False
        if wo and nx != no:
            return False
        if not 0 <= nx - no <= 1:
            return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = ["O  ","   ","   "]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validTicTacToe(["O  ", "   ", "   "])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = ["XOX"," X ","   "]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validTicTacToe(["XOX", " X ", "   "])))
    print()

    print('Example 3:')
    print('Input : ')
    print('board = ["XXX","   ","OOO"]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validTicTacToe(["XXX", "   ", "OOO"])))
    print()

    print('Example 4:')
    print('Input : ')
    print('board = ["XOX","O O","XOX"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validTicTacToe(["XOX", "O O", "XOX"])))
    print()

    pass
# @lc main=end