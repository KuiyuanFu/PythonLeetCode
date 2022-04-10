# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (69.09%)
# Likes:    1933
# Dislikes: 1994
# Total Accepted:    152.4K
# Total Submissions: 220.5K
# Testcase Example:  '[5,3,4,5]'
#
# Alice and Bob play a game with piles of stones. There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
#
# The objective of the game is to end with the most stones. The total number of
# stones across all the piles is odd, so there are no ties.
#
# Alice and Bob take turns, with Alice starting first. Each turn, a player
# takes the entire pile of stones either from the beginning or from the end of
# the row. This continues until there are no more piles left, at which point
# the person with the most stones wins.
#
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or
# false if Bob wins.
#
#
# Example 1:
#
#
# Input: piles = [5,3,4,5]
# Output: true
# Explanation:
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10
# points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we
# return true.
#
#
# Example 2:
#
#
# Input: piles = [3,7,2,3]
# Output: true
#
#
#
# Constraints:
#
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.
#
#
#

# @lc tags=dynamic-programming;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 两人从一组石块堆中拿石头，每次只能拿最左或最右的石块，A先拿，问A是否一定可以获胜。
# 总数为奇数，一定有胜负。
# DP。
# 保存每一段是的优势。
# 其实优势总是正的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[None for _ in range(length)] for _ in range(length)]

        for i in range(length):
            dp[i][i] = piles[i]

        for step in range(1, length):
            for l in range(length - step):
                r = l + step
                dp[l][r] = max(piles[l] - dp[l + 1][r],
                               piles[r] - dp[l][r - 1])
        return dp[0][-1] > 0

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('piles = [5,3,4,5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().stoneGame([5, 3, 4, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('piles = [3,7,2,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().stoneGame([3, 7, 2, 3])))
    print()

    pass
# @lc main=end