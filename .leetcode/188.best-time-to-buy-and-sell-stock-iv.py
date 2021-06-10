# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (30.48%)
# Likes:    2534
# Dislikes: 139
# Total Accepted:    186.7K
# Total Submissions: 610.7K
# Testcase Example:  '2\n[2,4,1]'
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the i^th day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete at most k
# transactions.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
#
#
# Example 2:
#
#
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit
# = 3-0 = 3.
#
#
#
# Constraints:
#
#
# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 股票交易k次，最大收益。
# 动态规划，每一次记录当前利润，和买入价格。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[prices[0], 0] for _ in range(k + 1)]
        for i in range(1, len(prices)):
            for d in reversed(range(1, len(dp))):
                dp[d][0] = min(dp[d][0], -dp[d - 1][1] + prices[i])
                dp[d][1] = max(dp[d][1], prices[i] - dp[d][0])
        return dp[-1][-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().maxProfit(1, [2, 1])))
    print('Example 1:')
    print('Input : ')
    print('k = 2, prices = [2,4,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxProfit(2, [2, 4, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 2, prices = [3,2,6,5,0,3]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3])))
    print()

    pass
# @lc main=end