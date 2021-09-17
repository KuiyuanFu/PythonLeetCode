# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (49.47%)
# Likes:    2340
# Dislikes: 126
# Total Accepted:    96.2K
# Total Submissions: 194.3K
# Testcase Example:  '[1,5,2]'
#
# You are given an integer array nums. Two players are playing a game with this
# array: player 1 and player 2.
#
# Player 1 and player 2 take turns, with player 1 starting first. Both players
# start the game with a score of 0. At each turn, the player takes one of the
# numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1])
# which reduces the size of the array by 1. The player adds the chosen number
# to their score. The game ends when there are no more elements in the array.
#
# Return true if Player 1 can win the game. If the scores of both players are
# equal, then player 1 is still the winner, and you should also return true.
# You may assume that both players are playing optimally.
#
#
# Example 1:
#
#
# Input: nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If
# player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return false.
#
#
# Example 2:
#
#
# Input: nums = [1,5,233,7]
# Output: true
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 10^7
#
#
#

# @lc tags=dynamic-programming;minimax

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 预测胜者，两个玩家，给定分数数组，每次取第一个或最后一个，问先手玩家是否分数一定大于等于后手玩家。
# 动态规划。数组长度为1时，先手分数就为这个值，后手为零；若长度大于一，那么先手值为选首尾加上对应后手分数的较大值。
#
# @lc idea=end

# @lc group=dynamic-programming;minimax

# @lc rank=10


# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[None for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = [nums[i], 0]
        for step in range(2, length + 1):
            for r in range(step - 1, length):
                l = r - step + 1
                t1 = dp[l][r - 1]
                t2 = dp[l + 1][r]
                if nums[l] + t2[1] > nums[r] + t1[1]:
                    dp[l][r] = [nums[l] + t2[1], t2[0]]
                else:
                    dp[l][r] = [nums[r] + t1[1], t1[0]]

        t = dp[0][-1]
        return t[0] >= t[1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,5,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().PredictTheWinner([1, 5, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,5,233,7]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().PredictTheWinner([1, 5, 233, 7])))
    print()
    print(str(Solution().PredictTheWinner([0])))
    pass
# @lc main=end