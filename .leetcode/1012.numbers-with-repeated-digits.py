# @lc app=leetcode id=1012 lang=python3
#
# [1012] Numbers With Repeated Digits
#
# https://leetcode.com/problems/numbers-with-repeated-digits/description/
#
# algorithms
# Hard (40.39%)
# Likes:    521
# Dislikes: 68
# Total Accepted:    11.1K
# Total Submissions: 27.4K
# Testcase Example:  '20'
#
# Given an integer n, return the number of positive integers in the range [1,
# n] that have at least one repeated digit.
#
#
# Example 1:
#
#
# Input: n = 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit
# is 11.
#
#
# Example 2:
#
#
# Input: n = 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are
# 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
#
#
# Example 3:
#
#
# Input: n = 1000
# Output: 262
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

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n，求小于等于n的整数中，有相同数字的个数。
# 阶乘获得数量。
#
# @lc idea=end

# @lc group=math

# @lc rank=10


# @lc code=start
class Solution:

    def numDupDigitsAtMostN(self, n: int) -> int:

        def get1(n: int):
            nn1 = n - 1
            return 9 * (10**nn1 - (factorial(9) // factorial(9 - nn1)))

        def get2(n: int, r: int):
            if r == 0:
                return 0

            n1 = 10**r
            n2 = (factorial(10 - n) // (factorial(10 - n - r)))
            re = n1 - n2
            return re

        def get3(r: int):
            return 10**r

        zeros = [get1(n) for n in range(1, 11)]

        ns = str(n)
        length = len(ns)
        res = sum(zeros[:len(ns) - 1])

        p = ''
        nss = '0123456789'
        f = False
        for c in ns:

            n1, n2 = len(p) + 1, length - len(p) - 1
            t1, t2 = get3(n2), get2(n1, n2)
            if f:
                idx = nss.index(c)
                res += idx * t1
            else:
                for s in nss:
                    if s == '0' and len(p) == 0:
                        continue
                    if s == c:
                        break
                    if s in p:
                        res += t1
                    else:
                        res += t2
            if c in p:
                f = True
            p = p + c

        if f:
            res += 1
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 11')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numDupDigitsAtMostN(11)))
    print('Example 1:')
    print('Input : ')
    print('n = 12')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numDupDigitsAtMostN(12)))
    print()
    print('Example 1:')
    print('Input : ')
    print('n = 20')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numDupDigitsAtMostN(20)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 100')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().numDupDigitsAtMostN(100)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 1000')
    print('Exception :')
    print('262')
    print('Output :')
    print(str(Solution().numDupDigitsAtMostN(1000)))
    print()

    pass
# @lc main=end