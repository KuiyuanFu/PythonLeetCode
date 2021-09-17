# @lc app=leetcode id=488 lang=python3
#
# [488] Zuma Game
#
# https://leetcode.com/problems/zuma-game/description/
#
# algorithms
# Hard (37.71%)
# Likes:    309
# Dislikes: 341
# Total Accepted:    18.7K
# Total Submissions: 49.4K
# Testcase Example:  '"WRRBBW"\n"RB"'
#
# You are playing a variation of the game Zuma.
#
# In this variation of Zuma, there is a single row of colored balls on a board,
# where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or
# white 'W'. You also have several colored balls in your hand.
#
# Your goal is to clear all of the balls from the board. On each turn:
#
#
# Pick any ball from your hand and insert it in between two balls in the row or
# on either end of the row.
# If there is a group of three or more consecutive balls of the same color,
# remove the group of balls from the board.
#
# If this removal causes more groups of three or more of the same color to
# form, then continue removing each group until there are none
# left.
#
#
# If there are no more balls on the board, then you win the game.
# Repeat this process until you either win or do not have any more balls in
# your hand.
#
#
# Given a string board, representing the row of balls on the board, and a
# string hand, representing the balls in your hand, return the minimum number
# of balls you have to insert to clear all the balls from the board. If you
# cannot clear all the balls from the board using the balls in your hand,
# return -1.
#
#
# Example 1:
#
#
# Input: board = "WRRBBW", hand = "RB"
# Output: -1
# Explanation: It is impossible to clear all the balls. The best you can do is:
# - Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
# - Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
# There are still balls remaining on the board, and you are out of balls to
# insert.
#
# Example 2:
#
#
# Input: board = "WWRRBBWW", hand = "WRBRW"
# Output: 2
# Explanation: To make the board empty:
# - Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
# - Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
# 2 balls from your hand were needed to clear the board.
#
#
# Example 3:
#
#
# Input: board = "G", hand = "GGGGG"
# Output: 2
# Explanation: To make the board empty:
# - Insert 'G' so the board becomes GG.
# - Insert 'G' so the board becomes GGG. GGG -> empty.
# 2 balls from your hand were needed to clear the board.
#
#
# Example 4:
#
#
# Input: board = "RBYYBBRRB", hand = "YRBGB"
# Output: 3
# Explanation: To make the board empty:
# - Insert 'Y' so the board becomes RBYYYBBRRB. RBYYYBBRRB -> RBBBRRB -> RRRB
# -> B.
# - Insert 'B' so the board becomes BB.
# - Insert 'B' so the board becomes BBB. BBB -> empty.
# 3 balls from your hand were needed to clear the board.
#
#
#
# Constraints:
#
#
# 1 <= board.length <= 16
# 1 <= hand.length <= 5
# board and hand consist of the characters 'R', 'Y', 'B', 'G', and 'W'.
# The initial row of balls on the board will not have any groups of three or
# more consecutive balls of the same color.
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 祖玛游戏，一列，给定可以使用的球，任意顺序。求最少清除次数。不能清除返回0.
# 直接暴力试试。竟然接受了。
# 消除的时候，逻辑错了。。
#
# @lc idea=end

# @lc group=depth-first-search

# @lc rank=10


# @lc code=start
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        buffer = {}
        ds = 'RYBGW'
        hand = [hand.count(c) for c in ds]
        ds = list(enumerate(ds))

        def remove(s, i):
            l, r = i, i
            length = len(s)
            while True:
                if l < 0 or r >= length:
                    break
                if s[l] != s[r]:
                    break
                c = s[l]

                n = 1 if l == r else 2
                lt, rt = l, r
                while lt - 1 >= 0 and s[lt - 1] == c:
                    lt -= 1
                    n += 1
                while rt + 1 < length and s[rt + 1] == c:
                    rt += 1
                    n += 1
                if n >= 3:
                    l = lt - 1
                    r = rt + 1
                else:
                    break
            # 这个位置出错了。 不加这条，会导致结果多一个字符。
            if l == r:
                l -= 1
            return s[:l + 1] + s[r:]

        def recur(b: str):
            if b == '':
                return 0
            if sum(hand) == 0:
                return -1
            key = tuple([b, *hand])
            if key in buffer:
                return buffer[key]
            res = 6

            for i, hc in ds:
                if hand[i] == 0:
                    continue
                hand[i] -= 1

                t = recur(remove(hc + b, 0))
                if t != -1 and t < res:
                    res = t
                for j in range(1, len(b) + 1):
                    t = recur(remove(b[:j] + hc + b[j:], j))
                    if t != -1 and t < res:
                        res = t
                hand[i] += 1

            if res == 6:
                res = -1
            else:
                res += 1
            buffer[key] = res
            return res

        return recur(board)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('board = "WRRBBW", hand = "RB"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findMinStep("WRRBBW", "RB")))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = "WWRRBBWW", hand = "WRBRW"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMinStep("WWRRBBWW", "WRBRW")))
    print()

    print('Example 3:')
    print('Input : ')
    print('board = "G", hand = "GGGGG"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMinStep("G", "GGGGG")))
    print()

    print('Example 4:')
    print('Input : ')
    print('board = "RBYYBBRRB", hand = "YRBGB"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findMinStep("RBYYBBRRB", "YRBGB")))
    print()

    pass
# @lc main=end