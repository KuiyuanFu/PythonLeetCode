# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (59.22%)
# Likes:    3189
# Dislikes: 84
# Total Accepted:    132K
# Total Submissions: 220.1K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day, and an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like, but you need to pay the transaction fee for each
# transaction.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
#
# Example 2:
#
#
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 5 * 10^4
# 1 <= prices[i] < 5 * 10^4
# 0 <= fee < 5 * 10^4
#
#
#

# @lc tags=array;dynamic-programming;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 交易。
# 动态规划。
# 每天其实就两个状态，一个是持有，一个空仓。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        h, e = -50000 - fee, 0
        for p in prices:
            h, e = max(h, e - p - fee), max(e, h + p)
        return e
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [1,3,2,8,4,9], fee = 2')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('prices = [1,3,7,5,10,3], fee = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3)))
    print()

    pass
# @lc main=end