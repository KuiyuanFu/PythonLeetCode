# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (58.92%)
# Likes:    4206
# Dislikes: 2011
# Total Accepted:    833K
# Total Submissions: 1.4M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
#
#
# Example 2:
#
#
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
#
#
# Example 3:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e., max profit = 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
#
#
#

# @lc tags=array;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定股票每天的价格，选择一天买，之后的一天卖，最大收益。
# 可以交易多次。
# 直接计算，如果后一天的价格比前一天的高，那就可以交易，连续两天交易可以合并成一次，所以不影响结果。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
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
    print('7')
    print()

    print('Example 2:')
    print('Input : ')
    print('prices = [1,2,3,4,5]')
    print('Output :')
    print(str(Solution().maxProfit([1, 2, 3, 4, 5])))
    print('Exception :')
    print('4')
    print()

    print('Example 3:')
    print('Input : ')
    print('prices = [7,6,4,3,1]')
    print('Output :')
    print(str(Solution().maxProfit([7, 6, 4, 3, 1])))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end