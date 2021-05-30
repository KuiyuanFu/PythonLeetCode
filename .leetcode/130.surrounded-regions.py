# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (29.92%)
# Likes:    2844
# Dislikes: 795
# Total Accepted:    303.4K
# Total Submissions: 1M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
#
# Example 1:
#
#
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is
# not on the border and it is not connected to an 'O' on the border will be
# flipped to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#
#

# @lc tags=depth-first-search;breadth-first-search;union-find

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维数组，有X与O两种类型，如果O被X包围了，那么就将O变为X。
# 思路就是以四周的O开始，遍历相邻结点，遍历到了O保留，其他的全置为X。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        q = []
        for i in range(rows):
            q.append((i, 0))
            q.append((i, cols - 1))
        for j in range(cols):
            q.append((0, j))
            q.append((rows - 1, j))
        while q:
            i, j = q.pop()
            if 0 <= i < rows and 0 <= j < cols:
                if board[i][j] == 'O':
                    board[i][j] = 'T'
                    q.append((i + 1, j))
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                pass

        return board
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'board =[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
    )
    print('Exception :')
    print(
        '[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]'
    )
    print('Output :')
    print(
        str(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"],
                              ["X", "X", "O", "X"], ["X", "O", "X", "X"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [["X"]]')
    print('Exception :')
    print('[["X"]]')
    print('Output :')
    print(str(Solution().solve([["X"]])))
    print()

    pass
# @lc main=end