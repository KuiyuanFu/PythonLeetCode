# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (41.07%)
# Likes:    755
# Dislikes: 355
# Total Accepted:    24.2K
# Total Submissions: 58.3K
# Testcase Example:  '3'
#
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You
# may rotate these shapes.
#
# Given an integer n, return the number of ways to tile an 2 x n board. Since
# the answer may be very large, return it modulo 10^9 + 7.
#
# In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#

# @lc tags=array;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 两个图形组合排满。
# dp。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        s = [
            [1, 0, 0, 1],
        ]
        while len(s) < n:
            l = s[-1]
            s.append([
                sum(l) % 1000000007,
                (l[2] + l[3]) % 1000000007,
                (l[1] + l[3]) % 1000000007,
                l[0],
            ])
        return s[n - 1][0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().numTilings(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numTilings(1)))
    print()
    print('Example 2:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().numTilings(4)))
    print()

    pass
# @lc main=end