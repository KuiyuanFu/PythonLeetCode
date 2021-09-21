# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (54.25%)
# Likes:    3819
# Dislikes: 83
# Total Accepted:    225.1K
# Total Submissions: 413K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the number of combinations that make up that amount. If that amount of
# money cannot be made up by any combination of the coins, return 0.
#
# You may assume that you have an infinite number of each kind of coin.
#
# The answer is guaranteed to fit into a signed 32-bit integer.
#
#
# Example 1:
#
#
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# Example 2:
#
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
#
# Example 3:
#
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 硬币，达到目标的组合数量。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort(reverse=True)

        @Memoize
        def recur(idx, target):
            if target == 0:
                return 1
            if idx == len(coins):
                return 0
            coin = coins[idx]
            cntMax = target // coin
            res = 0
            for cnt in range(cntMax + 1):
                res += recur(idx + 1, target - cnt * coin)
            return res

        return recur(0, amount)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('amount = 5, coins = [1,2,5]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().change(5, [1, 2, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('amount = 3, coins = [2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().change(3, [2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('amount = 10, coins = [10]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().change(10, [10])))
    print()

    pass
# @lc main=end