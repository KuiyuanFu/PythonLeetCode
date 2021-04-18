# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.94%)
# Likes:    1734
# Dislikes: 6749
# Total Accepted:    360.1K
# Total Submissions: 2.1M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) =
# -2.
#
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
# problem, assume that your function returns 2^31 − 1 when the division result
# overflows.
#
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
#
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
#
#
# Example 3:
#
#
# Input: dividend = 0, divisor = 1
# Output: 0
#
#
# Example 4:
#
#
# Input: dividend = 1, divisor = 1
# Output: 1
#
#
#
# Constraints:
#
#
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
#
#
#

# @lc tags=math;binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 除法，使用移位算法，先将数变为负的，防止溢出。每次都是将测试除数提高两倍时，看被除数是否够减，若够减则除数翻倍，统计有多少次。之后每次都是若够减，则减，否则将除数减半。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        doubled = 0
        # 是否异号
        minus = (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0)

        # 都转为负数，防止溢出
        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = - divisor

        # 移位，直到除数是被除数的一半以上
        while dividend >> 1 <= divisor:
            divisor <<= 1
            doubled += 1

        # 依次减去，若是够减，则加上对应的幂次数
        while doubled >= 0:
            if dividend <= divisor:
                dividend -= divisor
                quotient -= 1 << doubled
            divisor >>= 1
            doubled -= 1
        if minus:
            return quotient
        if quotient == - 2 ** 31:
            return 2 ** 31-1
        return -quotient


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('dividend = 10, divisor = 3')
    print('Output :')
    print(str(Solution().divide(10,3)))
    print('Exception :')
    print('3')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('dividend = 7, divisor = -3')
    print('Output :')
    print(str(Solution().divide(7,-3)))
    print('Exception :')
    print('-2')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('dividend = 0, divisor = 1')
    print('Output :')
    print(str(Solution().divide(0,1)))
    print('Exception :')
    print('0')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('dividend = 1, divisor = 1')
    print('Output :')
    print(str(Solution().divide(1,1)))
    print('Exception :')
    print('1')
    print()
    
    pass
# @lc main=end