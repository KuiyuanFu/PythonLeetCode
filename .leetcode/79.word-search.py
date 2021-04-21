# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (37.26%)
# Likes:    5531
# Dislikes: 242
# Total Accepted:    648.6K
# Total Submissions: 1.7M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#

# @lc tags=array;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符二维矩阵，再给定一个目标字符串，判断目标字符串是否可以在矩阵中找到，字符串中相邻的两个字符必须在矩阵中相邻。
# 朴素的想法就是一次遍历，之后回溯法。
# 效率很低。加上先判断是否可能存在解，就快了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.cols = len(board[0])
        self.rows = len(board)
        self.n = len(word) - 1

        # 判断是否可能存在解
        d = {}
        for i in range(self.rows):
            for j in range(self.cols):
                d[board[i][j]] = d.get(board[i][j], 0) + 1
        for c in word:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False

        # 标志位
        self.visited = [[False for _ in range(self.cols)]
                        for _ in range(self.rows)]
        self.board = board
        self.word = word
        self.forward = [0, 1, 0, -1, 0]
        # 确定起始位置
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0] and self.recur(i, j, 0):
                    return True
        return False
        pass

    def recur(self, i, j, index):
        if index == self.n:
            return True
        self.visited[i][j] = True

        for k in range(4):
            it = i + self.forward[k]
            jt = j + self.forward[k + 1]
            if 0 <= it < self.rows and 0 <= jt < self.cols:
                if self.visited[it][jt] == False and self.board[it][
                        jt] == self.word[index + 1]:
                    if self.recur(it, jt, index + 1):
                        return True

        self.visited[i][j] = False
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word= "ABCCED"'
    )
    print('Output :')
    print(
        str(Solution().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED")))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word= "SEE"'
    )
    print('Output :')
    print(
        str(Solution().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE")))
    print('Exception :')
    print('true')
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word= "ABCB"'
    )
    print('Output :')
    print(
        str(Solution().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB")))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end