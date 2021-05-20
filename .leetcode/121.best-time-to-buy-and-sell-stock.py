# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.89%)
# Likes:    8581
# Dislikes: 368
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#

# @lc tags=array;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定股票每天的价格，选择一天买，之后的一天卖，最大收益。
# 直接动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        priceMin = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            priceMin = min(priceMin, prices[i])
            profit = max(profit, prices[i] - priceMin)
        return profit

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [7,1,5,3,6,4]')
    print('Output :')
    print(str(Solution().maxProfit([7, 1, 5, 3, 6, 4])))
    print('Exception :')
    print('5')
    print()

    print('Example 2:')
    print('Input : ')
    print('prices = [7,6,4,3,1]')
    print('Output :')
    print(str(Solution().maxProfit([7, 6, 4, 3, 1])))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end