# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (29.73%)
# Likes:    1545
# Dislikes: 248
# Total Accepted:    67.1K
# Total Submissions: 226K
# Testcase Example:  '10\n11'
#
# In the "100 game" two players take turns adding, to a running total, any
# integer from 1 to 10. The player who first causes the running total to reach
# or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of
# numbers from 1 to 15 without replacement until they reach a total >= 100.
#
# Given two integers maxChoosableInteger and desiredTotal, return true if the
# first player to move can force a win, otherwise, return false. Assume both
# players play optimally.
#
#
# Example 1:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
#
#
# Example 2:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
#
#
# Example 3:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300
#
#
#

# @lc tags=dynamic-programming;minimax

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 游戏，谁先使两者总计达到目标谁赢，每个数字只能使用一次。
# 问给定目标及范围，第一个人是否一定会获胜。
#
# 赢的条件是，当前值加上可选值大于等于目标值。对方赢的条件也是一样的，那么对方能达到的最远值是，选择值，加上剩余的最大值。
# 递归，备忘录。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        buffer = {}

        def recur(cands, target):
            t = tuple(cands)
            if t in buffer:
                return buffer[t]
            res = False
            # choose the biggest interget can reach the target
            if cands[-1] >= target:
                res = True
            else:
                for i in range(len(cands)):
                    if not recur(cands[:i] + cands[i + 1:], target - cands[i]):
                        res = True
                        break

            buffer[t] = res
            return res

        if (1 + maxChoosableInteger) // 2 * maxChoosableInteger < desiredTotal:
            return False

        cands = list(range(1, maxChoosableInteger + 1))
        return recur(cands, desiredTotal)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('maxChoosableInteger = 10, desiredTotal = 11')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canIWin(10, 11)))
    print()

    print('Example 2:')
    print('Input : ')
    print('maxChoosableInteger = 10, desiredTotal = 0')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canIWin(10, 0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('maxChoosableInteger = 10, desiredTotal = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canIWin(10, 1)))
    print()

    pass
# @lc main=end