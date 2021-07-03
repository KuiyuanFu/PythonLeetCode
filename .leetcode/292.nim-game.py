# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.13%)
# Likes:    821
# Dislikes: 1931
# Total Accepted:    249.4K
# Total Submissions: 451.9K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend:
#
#
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the
# heap.
# The one who removes the last stone is the winner.
#
#
# Given n, the number of stones in the heap, return true if you can win the
# game assuming both you and your friend play optimally, otherwise return
# false.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last
# stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last
# stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: true
#
#
# Example 3:
#
#
# Input: n = 2
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=brainteaser;minimax

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 拿取游戏，两人依次拿1-3个石头，谁拿到最后一个就获胜。
# 判断先拿的人是否可以获胜。
# 直接dp。我可以选择拿1-3个石头，这样就对应对方的三个结果，若有一个对方必输，那么我就必赢。
# 直接数学方法会更快。dp会超时。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().canWinNim(1000)))
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canWinNim(4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canWinNim(1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canWinNim(2)))
    print()

    pass
# @lc main=end