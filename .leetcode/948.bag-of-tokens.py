# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#
# https://leetcode.com/problems/bag-of-tokens/description/
#
# algorithms
# Medium (46.34%)
# Likes:    765
# Dislikes: 298
# Total Accepted:    41.4K
# Total Submissions: 89.4K
# Testcase Example:  '[100]\n50'
#
# You have an initial power of power, an initial score of 0, and a bag of
# tokens where tokens[i] is the value of the i^th token (0-indexed).
#
# Your goal is to maximize your total score by potentially playing each token
# in one of two ways:
#
#
# If your current power is at least tokens[i], you may play the i^th token face
# up, losing tokens[i] power and gaining 1 score.
# If your current score is at least 1, you may play the i^th token face down,
# gaining tokens[i] power and losing 1 score.
#
#
# Each token may be played at most once and in any order. You do not have to
# play all the tokens.
#
# Return the largest possible score you can achieve after playing any number of
# tokens.
#
#
# Example 1:
#
#
# Input: tokens = [100], power = 50
# Output: 0
# Explanation: Playing the only token in the bag is impossible because you
# either have too little power or too little score.
#
#
# Example 2:
#
#
# Input: tokens = [100,200], power = 150
# Output: 1
# Explanation: Play the 0^th token (100) face up, your power becomes 50 and
# score becomes 1.
# There is no need to play the 1^st token since you cannot play it face up to
# add to your score.
#
#
# Example 3:
#
#
# Input: tokens = [100,200,300,400], power = 200
# Output: 2
# Explanation: Play the tokens in this order to get a score of 2:
# 1. Play the 0^th token (100) face up, your power becomes 100 and score
# becomes 1.
# 2. Play the 3^rd token (400) face down, your power becomes 500 and score
# becomes 0.
# 3. Play the 1^st token (200) face up, your power becomes 300 and score
# becomes 1.
# 4. Play the 2^nd token (300) face up, your power becomes 0 and score becomes
# 2.
#
#
#
# Constraints:
#
#
# 0 <= tokens.length <= 1000
# 0 <= tokens[i], power < 10^4
#
#
#

# @lc tags=Unknown

# @lc imports=start
from lib2to3.pgen2 import token
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定初始能量，并给定能量数组，对于每一个元素可以花费能量获得一个分数，也可通过一个分数获得能量，求最多的分数。
# 花费最少能量买分，并用分买能量。
# 排序，用三个索引指向买、拥有、卖的位置。
# 记录拥有的最大能量，及拥有后的能量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        tokens.sort()

        res = 0
        powerMax, powerNow = power, power
        # buy,own,sall
        l, m, r = 0, 0, len(tokens) - 1
        score = 0
        while True:
            while m <= r and powerNow >= tokens[m]:
                score += 1
                powerNow -= tokens[m]
                m += 1
            res = max(res, score)
            if powerMax >= tokens[l] and m < r:

                powerNow += tokens[r]
                powerMax += tokens[r] - tokens[l]
                score -= 1
                l += 1
                r -= 1
            else:
                break
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('tokens = [100], power = 50')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().bagOfTokensScore([100], 50)))
    print()

    print('Example 2:')
    print('Input : ')
    print('tokens = [100,200], power = 150')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().bagOfTokensScore([100, 200], 150)))
    print()

    print('Example 3:')
    print('Input : ')
    print('tokens = [100,200,300,400], power = 200')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().bagOfTokensScore([100, 200, 300, 400], 200)))
    print()

    print('Example 3:')
    print('Input : ')
    print('tokens = [91,4,75,70,66,71,91,64,37,54], power = 20')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().bagOfTokensScore(
            [91, 4, 75, 70, 66, 71, 91, 64, 37, 54], 20)))
    print()

    pass
# @lc main=end