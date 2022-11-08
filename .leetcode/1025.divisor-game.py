# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#
# https://leetcode.com/problems/divisor-game/description/
#
# algorithms
# Easy (67.13%)
# Likes:    1633
# Dislikes: 3511
# Total Accepted:    181.8K
# Total Submissions: 270.8K
# Testcase Example:  '2'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number n on the chalkboard. On each player's turn, that
# player makes a move consisting of:
#
#
# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
#
#
# Also, if a player cannot make a move, they lose the game.
#
# Return true if and only if Alice wins the game, assuming both players play
# optimally.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
#
#
# Example 2:
#
#
# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 除法游戏，有一个数n，每次选择一个0<x<n可以被其整除的数，减去这个。谁没有数，就输了。求第一个人胜的概率。
# dp
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def divisorGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            dp.append(False)
            for j in range(1, i):
                if i % j == 0:
                    k = i - j
                    if dp[k] == False:
                        dp[i] = True
                        break

        return dp[n]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().divisorGame(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().divisorGame(3)))
    print()

    pass
# @lc main=end