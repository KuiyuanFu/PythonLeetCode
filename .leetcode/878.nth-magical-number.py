# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#
# https://leetcode.com/problems/nth-magical-number/description/
#
# algorithms
# Hard (35.76%)
# Likes:    957
# Dislikes: 134
# Total Accepted:    29K
# Total Submissions: 81.2K
# Testcase Example:  '1\n2\n3'
#
# A positive integer is magical if it is divisible by either a or b.
#
# Given the three integers n, a, and b, return the n^th magical number. Since
# the answer may be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1, a = 2, b = 3
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 4, a = 2, b = 3
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
# 2 <= a, b <= 4 * 10^4
#
#
#

# @lc tags=string

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 求第n个，可以整除a或b的数
# 求最大公约数，之后求最大公倍数，再之后就可以求modular了。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        lcmab = a * b // gcd(a, b)
        mulNumberCount = lcmab // a + lcmab // b - 1
        base = lcmab * (n // mulNumberCount)
        modular = n % mulNumberCount

        l, r = 0, lcmab
        while l < r:
            m = (l + r) // 2
            mc = m // a + m // b
            if mc >= modular:
                r = m
            elif mc < modular:
                l = m + 1
        return (base + l) % 1000000007
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1, a = 2, b = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().nthMagicalNumber(1, 2, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 4, a = 2, b = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().nthMagicalNumber(4, 2, 3)))
    print()

    pass
# @lc main=end