# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (62.11%)
# Likes:    1251
# Dislikes: 34
# Total Accepted:    63.4K
# Total Submissions: 101.4K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty
# square represented by 0. A move consists of choosing 0 and a 4-directionally
# adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
#
# Given the puzzle board board, return the least number of moves required so
# that the state of the board is solved. If it is impossible for the state of
# the board to be solved, return -1.
#
#
# Example 1:
#
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
#
#
# Example 2:
#
#
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
#
#
# Example 3:
#
#
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
#
#
# Example 4:
#
#
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
#
#
#
# Constraints:
#
#
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 华容道。
# 深度优先。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visted = set()
        ls = list(product(range(2), range(3)))

        def boardToKey(board):
            return tuple(board[i][j] for i, j in ls)

        def deepCopy(board):
            return [board[0].copy(), board[1].copy()]

        target = boardToKey([[1, 2, 3], [4, 5, 0]])

        if boardToKey(board) == target:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        res = 0

        for i, j in ls:
            if board[i][j] == 0:
                break
        s = [(board, i, j)]
        while s:
            res += 1
            ns = []
            for b, i, j in s:
                for oi, oj in directions:
                    ni, nj = i + oi, j + oj

                    if 0 <= ni < 2 and 0 <= nj < 3:
                        bc = deepCopy(b)
                        bc[i][j], bc[ni][nj] = bc[ni][nj], bc[i][j]
                        bck = boardToKey(bc)
                        if bck == target:
                            return res
                        if bck not in visted:
                            ns.append((bc, ni, nj))
                            visted.add(bck)
            s = ns

        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = [[1,2,3],[4,0,5]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [[1,2,3],[5,4,0]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('board = [[4,1,2],[5,0,3]]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]])))
    print()

    print('Example 4:')
    print('Input : ')
    print('board = [[3,2,4],[1,5,0]]')
    print('Exception :')
    print('14')
    print('Output :')
    print(str(Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]])))
    print()

    pass
# @lc main=end