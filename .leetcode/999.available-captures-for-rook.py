# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#
# https://leetcode.com/problems/available-captures-for-rook/description/
#
# algorithms
# Easy (67.75%)
# Likes:    495
# Dislikes: 583
# Total Accepted:    53.4K
# Total Submissions: 78.9K
# Testcase Example:  '[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]'
#
# On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number
# of white bishops 'B', black pawns 'p', and empty squares '.'.
#
# When the rook moves, it chooses one of four cardinal directions (north, east,
# south, or west), then moves in that direction until it chooses to stop,
# reaches the edge of the board, captures a black pawn, or is blocked by a
# white bishop. A rook is considered attacking a pawn if the rook can capture
# the pawn on the rook's turn. The number of available captures for the white
# rook is the number of pawns that the rook is attacking.
#
# Return the number of available captures for the white rook.
#
#
# Example 1:
#
#
# Input: board =
# [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: In this example, the rook is attacking all the pawns.
#
#
# Example 2:
#
#
# Input: board =
# [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation: The bishops are blocking the rook from attacking any of the
# pawns.
#
#
# Example 3:
#
#
# Input: board =
# [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
#
#
#
# Constraints:
#
#
# board.length == 8
# board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'
#
#
#

# @lc tags=depth-first-search;union-find;graph

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 四个方向，遇到的第一个棋子可以被干掉，求最多可能干掉的数量。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        for i, j in product(range(rows), range(cols)):
            if board[i][j] == 'R':
                si, sj = i, j
                break

        res = 0
        ni, nj = si - 1, sj
        while ni >= 0 and board[ni][nj] == '.':
            ni -= 1
        if ni >= 0 and board[ni][nj] == 'p':
            res += 1

        ni, nj = si + 1, sj
        while ni < rows and board[ni][nj] == '.':
            ni += 1
        if ni < rows and board[ni][nj] == 'p':
            res += 1

        ni, nj = si, sj - 1
        while nj >= 0 and board[ni][nj] == '.':
            nj -= 1
        if nj >= 0 and board[ni][nj] == 'p':
            res += 1

        ni, nj = si, sj + 1
        while nj < cols and board[ni][nj] == '.':
            nj += 1
        if nj < cols and board[ni][nj] == 'p':
            res += 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'board =[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]'
    )
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numRookCaptures(
            [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "R", ".", ".", ".", "p"],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'board =[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]'
    )
    print('Exception :')
    print('0')
    print('Output :')
    print(
        str(Solution().numRookCaptures(
            [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", "p", "p", "p", "p", "p", ".", "."],
             [".", "p", "p", "B", "p", "p", ".", "."],
             [".", "p", "B", "R", "B", "p", ".", "."],
             [".", "p", "p", "B", "p", "p", ".", "."],
             [".", "p", "p", "p", "p", "p", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'board =[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]'
    )
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numRookCaptures(
            [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]])))
    print()

    pass
# @lc main=end