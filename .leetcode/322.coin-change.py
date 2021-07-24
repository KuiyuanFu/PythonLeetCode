# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (38.38%)
# Likes:    7686
# Dislikes: 210
# Total Accepted:    699.3K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Example 4:
#
#
# Input: coins = [1], amount = 1
# Output: 1
#
#
# Example 5:
#
#
# Input: coins = [1], amount = 2
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定硬币与目标数，求使用最少的硬币个数。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [amount + 1] * (amount + 1)
        counts[0] = 0
        for coin in coins:
            for i in range(amount - coin + 1):
                counts[i + coin] = min(counts[i + coin], counts[i] + 1)
        return -1 if counts[-1] == amount + 1 else counts[-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('coins = [1,2,5], amount = 11')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().coinChange([1, 2, 5], 11)))
    print()

    print('Example 2:')
    print('Input : ')
    print('coins = [2], amount = 3')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().coinChange([2], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('coins = [1], amount = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().coinChange([1], 0)))
    print()

    print('Example 4:')
    print('Input : ')
    print('coins = [1], amount = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().coinChange([1], 1)))
    print()

    print('Example 5:')
    print('Input : ')
    print('coins = [1], amount = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().coinChange([1], 2)))
    print()

    pass
# @lc main=end