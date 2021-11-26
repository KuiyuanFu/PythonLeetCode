# @lc app=leetcode id=782 lang=python3
#
# [782] Transform to Chessboard
#
# https://leetcode.com/problems/transform-to-chessboard/description/
#
# algorithms
# Hard (47.14%)
# Likes:    270
# Dislikes: 276
# Total Accepted:    14.4K
# Total Submissions: 27.8K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]'
#
# You are given an n x n binary grid board. In each move, you can swap any two
# rows with each other, or any two columns with each other.
#
# Return the minimum number of moves to transform the board into a chessboard
# board. If the task is impossible, return -1.
#
# A chessboard board is a board where no 0's and no 1's are 4-directionally
# adjacent.
#
#
# Example 1:
#
#
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation: One potential sequence of moves is shown.
# The first move swaps the first and second column.
# The second move swaps the second and third row.
#
#
# Example 2:
#
#
# Input: board = [[0,1],[1,0]]
# Output: 0
# Explanation: Also note that the board with 0 in the top left corner, is also
# a valid chessboard.
#
#
# Example 3:
#
#
# Input: board = [[1,0],[1,0]]
# Output: -1
# Explanation: No matter what sequence of moves you make, you cannot end with a
# valid chessboard.
#
#
#
# Constraints:
#
#
# n == board.length
# n == board[i].length
# 2 <= n <= 30
# board[i][j] is either 0 or 1.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 转换为棋盘。
# 根据性质，判断，每一行或列只能有两种情况。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        bs = [board, list(zip(*board))]
        res = 0
        for b in bs:
            d = {}
            for i in range(n):
                t = tuple(b[i])
                if t not in d:
                    d[t] = []
                d[t].append(i)
            # only two type
            if len(d) != 2:
                return -1
            # type count is same
            l1, l2 = list(d.keys())
            if abs(len(d[l1]) - len(d[l2])) > 1:
                return -1
            # value is unique
            for i in range(n):
                if l1[i] == l2[i]:
                    return -1
            # 0's count is same as 1's
            if abs(len(l1) - 2 * l1.count(0)) > 1:
                return -1
            # odd
            if n % 2 == 1:
                # must in even idx, start in 0
                if len(d[l1]) > len(d[l2]):
                    ls, idices = (l1, d[l1])
                else:
                    ls, idices = (l2, d[l2])
                for idx in idices:
                    if idx % 2 == 1:
                        res += 1
            # even
            else:
                idices = d[l1]
                r = 0
                for idx in idices:
                    if idx % 2 == 1:
                        r += 1
                # odd or even
                r = min(r, n // 2 - r)
                res += r

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0],
                                          [1, 0, 0, 1], [1, 0, 0, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [[0,1],[1,0]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().movesToChessboard([[0, 1], [1, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('board = [[1,0],[1,0]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().movesToChessboard([[1, 0], [1, 0]])))
    print()

    pass
# @lc main=end