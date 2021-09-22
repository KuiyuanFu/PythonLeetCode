# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
# https://leetcode.com/problems/minesweeper/description/
#
# algorithms
# Medium (62.89%)
# Likes:    1089
# Dislikes: 738
# Total Accepted:    95.8K
# Total Submissions: 151.8K
# Testcase Example:  '[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\n' +
# '[3,0]'
#
# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given an m x n char matrix board representing the game board
# where:
#
#
# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e.,
# above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed
# square, and
# 'X' represents a revealed mine.
#
#
# You are also given an integer array click where click = [clickr, clickc]
# represents the next click position among all the unrevealed squares ('M' or
# 'E').
#
# Return the board after revealing this position according to the following
# rules:
#
#
# If a mine 'M' is revealed, then the game is over. You should change it to
# 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to
# a revealed blank 'B' and all of its adjacent unrevealed squares should be
# revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then
# change it to a digit ('1' to '8') representing the number of adjacent
# mines.
# Return the board when no more squares will be revealed.
#
#
#
# Example 1:
#
#
# Input: board =
# [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],
# click = [3,0]
# Output:
# [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
#
#
# Example 2:
#
#
# Input: board =
# [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],
# click = [1,2]
# Output:
# [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 50
# board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
# click.length == 2
# 0 <= clickr < m
# 0 <= clickc < n
# board[clickr][clickc] is either 'M' or 'E'.
#
#
#

# @lc tags=depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 扫雷游戏。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),
                          (-1, 1), (-1, -1)]
            stack = [click]
            while stack:
                i, j = stack.pop()
                if board[i][j] == 'E':
                    n = 0
                    for oi, oj in directions:
                        ni, nj = i + oi, j + oj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if board[ni][nj] == 'M':
                                n += 1
                    if n == 0:
                        board[i][j] = 'B'
                        for oi, oj in directions:
                            ni, nj = i + oi, j + oj
                            if 0 <= ni < rows and 0 <= nj < cols:
                                stack.append((ni, nj))
                    else:
                        board[i][j] = str(n)

        return board


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'board =[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],click = [3,0]'
    )
    print('Exception :')
    print(
        '[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]'
    )
    print('Output :')
    print(
        str(Solution().updateBoard(
            [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
             ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]], [3, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'board =[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],click = [1,2]'
    )
    print('Exception :')
    print(
        '[["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]'
    )
    print('Output :')
    print(
        str(Solution().updateBoard(
            [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"],
             ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]], [1, 2])))
    print()

    pass
# @lc main=end