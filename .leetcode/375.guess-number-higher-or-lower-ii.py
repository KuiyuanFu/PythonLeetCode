# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
#
# algorithms
# Medium (43.32%)
# Likes:    1155
# Dislikes: 1572
# Total Accepted:    80.8K
# Total Submissions: 185.6K
# Testcase Example:  '10'
#
# We are playing the Guessing Game. The game will work as follows:
#
#
# I pick a number between 1 and n.
# You guess a number.
# If you guess the right number, you win the game.
# If you guess the wrong number, then I will tell you whether the number I
# picked is higher or lower, and you will continue guessing.
# Every time you guess a wrong number x, you will pay x dollars. If you run out
# of money, you lose the game.
#
#
# Given a particular n, return the minimum amount of money you need to
# guarantee a win regardless of what number I pick.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 16
# Explanation: The winning strategy is as follows:
# - The range is [1,10]. Guess 7.
# - If this is my number, your total is $0. Otherwise, you pay $7.
# - If my number is higher, the range is [8,10]. Guess 9.
# - If this is my number, your total is $7. Otherwise, you pay $9.
# - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 =
# $16.
# - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 =
# $16.
# - If my number is lower, the range is [1,6]. Guess 3.
# - If this is my number, your total is $7. Otherwise, you pay $3.
# - If my number is higher, the range is [4,6]. Guess 5.
# - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay
# $5.
# - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 =
# $15.
# - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 =
# $15.
# - If my number is lower, the range is [1,2]. Guess 1.
# - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay
# $1.
# - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 =
# $11.
# The worst case in all these scenarios is that you pay $16. Hence, you only
# need $16 to guarantee a win.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 0
# Explanation: There is only one possible number, so you can guess 1 and not
# have to pay anything.
#
#
# Example 3:
#
#
# Input: n = 2
# Output: 1
# Explanation: There are two possible numbers, 1 and 2.
# - Guess 1.
# - If this is my number, your total is $0. Otherwise, you pay $1.
# - If my number is higher, it must be 2. Guess 2. Your total is $1.
# The worst case is that you pay $1.
#
#
#
# Constraints:
#
#
# 1 <= n <= 200
#
#
#

# @lc tags=dynamic-programming;minimax

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 猜数字，每猜一次需要数字大小的代价，问保证猜中至少需要多少代价。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        t = n * n
        dp = [[t for _ in range(n + 1)] for _ in range(n + 1)]
        # step = 0
        for i in range(1, n + 1):
            dp[i][i] = 0
        # step = 1
        for i in range(1, n):
            dp[i][i + 1] = i
        for step in range(2, n):
            for l in range(1, n + 1 - step):
                r = l + step
                for m in range(l + 1, r):
                    dp[l][r] = min(dp[l][r],
                                   m + max(dp[l][m - 1], dp[m + 1][r]))
        return dp[1][n]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().getMoneyAmount(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().getMoneyAmount(1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().getMoneyAmount(2)))
    print()

    pass
# @lc main=end