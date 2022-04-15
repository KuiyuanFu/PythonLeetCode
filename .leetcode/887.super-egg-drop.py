# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#
# https://leetcode.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (27.17%)
# Likes:    2335
# Dislikes: 130
# Total Accepted:    44.6K
# Total Submissions: 164.3K
# Testcase Example:  '1\n2'
#
# You are given k identical eggs and you have access to a building with n
# floors labeled from 1 to n.
#
# You know that there exists a floor f where 0 <= f <= n such that any egg
# dropped at a floor higher than f will break, and any egg dropped at or below
# floor f will not break.
#
# Each move, you may take an unbroken egg and drop it from any floor x (where 1
# <= x <= n). If the egg breaks, you can no longer use it. However, if the egg
# does not break, you may reuse it in future moves.
#
# Return the minimum number of moves that you need to determine with certainty
# what the value of f is.
#
#
# Example 1:
#
#
# Input: k = 1, n = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1. If it breaks, we know that f = 0.
# Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
# If it does not break, then we know f = 2.
# Hence, we need at minimum 2 moves to determine with certainty what the value
# of f is.
#
#
# Example 2:
#
#
# Input: k = 2, n = 6
# Output: 3
#
#
# Example 3:
#
#
# Input: k = 3, n = 14
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= k <= 100
# 1 <= n <= 10^4
#
#
#

# @lc tags=heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定k个鸡蛋及最高台阶数，求最少扔下次数，求得鸡蛋完整的最高台阶。
#
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:

    def superEggDrop(self, eggNumber: int, floorNumber: int) -> int:
        eggLen = eggNumber + 1

        dp = [0] * eggLen
        dpn = [0] * eggLen
        moveNumber = 0
        while dp[-1] < floorNumber:
            moveNumber += 1

            for egg in range(1, eggLen):
                dpn[egg] = dp[egg - 1] + dp[egg] + 1

            dp, dpn = dpn, dp

        return moveNumber


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('k = 1, n = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().superEggDrop(1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 2, n = 6')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().superEggDrop(2, 6)))
    print()

    print('Example 3:')
    print('Input : ')
    print('k = 3, n = 14')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().superEggDrop(3, 14)))
    print()

    pass
# @lc main=end