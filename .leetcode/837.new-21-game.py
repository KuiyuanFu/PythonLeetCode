# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#
# https://leetcode.com/problems/new-21-game/description/
#
# algorithms
# Medium (36.00%)
# Likes:    921
# Dislikes: 600
# Total Accepted:    30.2K
# Total Submissions: 83.9K
# Testcase Example:  '10\n1\n10'
#
# Alice plays the following game, loosely based on the card game "21".
#
# Alice starts with 0 points and draws numbers while she has less than k
# points. During each draw, she gains an integer number of points randomly from
# the range [1, maxPts], where maxPts is an integer. Each draw is independent
# and the outcomes have equal probabilities.
#
# Alice stops drawing numbers when she gets k or more points.
#
# Return the probability that Alice has n or fewer points.
#
# Answers within 10^-5 of the actual answer are considered accepted.
#
#
# Example 1:
#
#
# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.
#
#
# Example 2:
#
#
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.
#
#
# Example 3:
#
#
# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278
#
#
#
# Constraints:
#
#
# 0 <= k <= n <= 10^4
# 1 <= maxPts <= 10^4
#
#
#

# @lc tags=string

# @lc imports=start
from audioop import maxpp
from imports import *

# @lc imports=end

# @lc idea=start
#
# 宽松的21点游戏，给定n、k、maxPts，起始点数为0，如果点数小于k，那么就随机获得一个小于等于maxPts的点数，问最后小于n的概率。
# 朴素想法是，记录每一个点数的概率，从小到大遍历，将此点数概率平均分给接下来的maxPts个点数。这样复杂度是 k*maxPts
# 进一步的想法是，对于从小到大遍历时的每一点数，索引为i，记录当前的概率p，已经分给之后的概率d = p / maxPts，再记录影响结束的位置 i+p，设dp[i+p] =d，之后再减去当前影响结束的概率 p -= dp[i] 。
#
#
# @lc idea=end

# @lc group=string

# @lc rank=8


# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1
        res = 0
        removePoint = [0] * (n + 1)
        removePoint[0] = 1
        prob = 1

        for i in range(k):
            pd = prob / maxPts
            prob += pd
            if i + maxPts <= n:
                removePoint[i + maxPts] = pd
            prob -= removePoint[i]
        for i in range(k, n + 1):
            res += prob
            prob -= removePoint[i]

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10, k = 1, maxPts = 10')
    print('Exception :')
    print('1.00000')
    print('Output :')
    print(str(Solution().new21Game(10, 1, 10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 6, k = 1, maxPts = 10')
    print('Exception :')
    print('0.60000')
    print('Output :')
    print(str(Solution().new21Game(6, 1, 10)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 21, k = 17, maxPts = 10')
    print('Exception :')
    print('0.73278')
    print('Output :')
    print(str(Solution().new21Game(21, 17, 10)))
    print('Exception :')
    print('0.13649')
    print('Output :')
    print(str(Solution().new21Game(5710, 5070, 8516)))
    print('Exception :')
    print('1.00000')
    print('Output :')
    print(str(Solution().new21Game(0, 0, 1)))
    print()
    print(str(Solution().new21Game(10000, 10000, 10000)))
    pass
# @lc main=end