# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (40.26%)
# Likes:    3581
# Dislikes: 91
# Total Accepted:    291.9K
# Total Submissions: 722.4K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# Find the maximum profit you can achieve. You may complete at most two
# transactions.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
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
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
# Example 4:
#
#
# Input: prices = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
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
# 最多执行两次交易。
# 现在考虑k次交易，也就是另一道进阶的题。
# 使用动态规划，就需要找到最优子结构。
# 首先，每一天，交易k次的最优收益，应该是交易k-1次收益 与 再交易一次的和。
# 这样就需要两个变量，一个交易k次的最大利润，另一个是第k次交易的起始金额。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        k = 2

        # 买入价 最大利润
        dp = [[prices[0], 0] for _ in range(k + 1)]
        for p in prices:
            # 倒序，防止数据被覆盖
            for i in range(k, 0, -1):
                # 第一个元素是买入价，包含了之前的利润
                dp[i][0] = min(dp[i][0], -dp[i - 1][1] + p)
                # 第二个是此时的利润
                dp[i][1] = max(dp[i][1], p - dp[i][0])
        return dp[-1][1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [3,3,5,0,0,3,1,4]')
    print('Output :')
    print(str(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])))
    print('Exception :')
    print('6')
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

    print('Example 4:')
    print('Input : ')
    print('prices = [1]')
    print('Output :')
    print(str(Solution().maxProfit([1])))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end