# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (46.23%)
# Likes:    754
# Dislikes: 79
# Total Accepted:    33.5K
# Total Submissions: 72.2K
# Testcase Example:  '10'
#
# An integer has monotone increasing digits if and only if each pair of
# adjacent digits x and y satisfy x <= y.
#
# Given an integer n, return the largest number that is less than or equal to n
# with monotone increasing digits.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 9
#
#
# Example 2:
#
#
# Input: n = 1234
# Output: 1234
#
#
# Example 3:
#
#
# Input: n = 332
# Output: 299
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求不大于n的所有数字中，每一位是递增数列的最大个数。
# 调整逆序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        from functools import reduce
        ds = [int(c) for c in str(n)]
        idx = len(ds) - 1
        idx9 = len(ds)
        while idx > 0:
            if ds[idx] < ds[idx - 1]:
                ds[idx - 1] -= 1
                idx9 = idx
            idx -= 1
        ds[idx9:] = [9] * len(ds[idx9:])
        return reduce(lambda x, y: x * 10 + y, ds)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().monotoneIncreasingDigits(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1234')
    print('Exception :')
    print('1234')
    print('Output :')
    print(str(Solution().monotoneIncreasingDigits(1234)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 332')
    print('Exception :')
    print('299')
    print('Output :')
    print(str(Solution().monotoneIncreasingDigits(332)))
    print()

    pass
# @lc main=end