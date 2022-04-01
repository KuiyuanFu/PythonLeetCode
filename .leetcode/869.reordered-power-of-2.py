# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (61.32%)
# Likes:    571
# Dislikes: 169
# Total Accepted:    40.6K
# Total Submissions: 66.2K
# Testcase Example:  '1'
#
# You are given an integer n. We reorder the digits in any order (including the
# original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this so that the resulting number is a
# power of two.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
#
#
# Example 2:
#
#
# Input: n = 10
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
#
#
#

# @lc tags=depth-first-search;union-find;graph

# @lc imports=start
from inspect import getblock
from imports import *

# @lc imports=end

# @lc idea=start
#
# 十进制数，重新排列，是2的幂。
# 计算所有2的幂，之后排列。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


def getKey(n: int):

    return ''.join(sorted([c for c in str(n)]))


def getBuf():
    buf = set()
    i = 1
    while i < 10**9:

        buf.add(getKey(i))
        i *= 2
    return buf


buf = getBuf()


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        return getKey(n) in buf

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().reorderedPowerOf2(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().reorderedPowerOf2(10)))
    print()

    pass
# @lc main=end