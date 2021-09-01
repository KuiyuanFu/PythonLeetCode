# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (43.06%)
# Likes:    1136
# Dislikes: 840
# Total Accepted:    206.5K
# Total Submissions: 479.2K
# Testcase Example:  '5'
#
# You have n coins and you want to build a staircase with these coins. The
# staircase consists of k rows where the i^th row has exactly i coins. The last
# row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you
# will build.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: Because the 3^rd row is incomplete, we return 2.
#
#
# Example 2:
#
#
# Input: n = 8
# Output: 3
# Explanation: Because the 4^th row is incomplete, we return 3.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=math;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数量n，求构造的完整台阶数，每一级比上一级使用多一个。
# 二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            m = (l + r + 1) // 2
            if (1 + m) * m // 2 <= n:
                l = m
            else:
                r = m - 1
        return l
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().arrangeCoins(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 8')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().arrangeCoins(8)))
    print()

    pass
# @lc main=end