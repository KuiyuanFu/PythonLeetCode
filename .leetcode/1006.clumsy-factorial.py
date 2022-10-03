# @lc app=leetcode id=1006 lang=python3
#
# [1006] Clumsy Factorial
#
# https://leetcode.com/problems/clumsy-factorial/description/
#
# algorithms
# Medium (54.72%)
# Likes:    238
# Dislikes: 261
# Total Accepted:    22.2K
# Total Submissions: 40.6K
# Testcase Example:  '4'
#
# The factorial of a positive integer n is the product of all positive integers
# less than or equal to n.
#
#
# For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
#
#
# We make a clumsy factorial using the integers in decreasing order by swapping
# out the multiply operations for a fixed rotation of operations with multiply
# '*', divide '/', add '+', and subtract '-' in this order.
#
#
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
#
#
# However, these operations are still applied using the usual order of
# operations of arithmetic. We do all multiplication and division steps before
# any addition or subtraction steps, and multiplication and division steps are
# processed left to right.
#
# Additionally, the division that we use is floor division such that 10 * 9 / 8
# = 90 / 8 = 11.
#
# Given an integer n, return the clumsy factorial of n.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
#
#
# Example 2:
#
#
# Input: n = 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc tags=hash-table;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 笨拙的阶乘。
# 负数模
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def clumsy(self, n: int) -> int:

        res = 1
        if n > 0:
            res = n
            n -= 1
        if n > 0:
            res = res * n
            n -= 1
        if n > 0:
            res = res // n
            n -= 1
        if n > 0:
            res = res + n
            n -= 1

        while n > 0:
            t = n
            n -= 1
            if n > 0:
                t = t * n
                n -= 1
            if n > 0:
                t = t // n
                n -= 1
            if n > 0:
                t = t - n
                n -= 1
            res -= t
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().clumsy(4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().clumsy(10)))
    print()

    pass
# @lc main=end