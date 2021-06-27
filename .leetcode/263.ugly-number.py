# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (41.67%)
# Likes:    834
# Dislikes: 835
# Total Accepted:    246.3K
# Total Submissions: 591.4K
# Testcase Example:  '6'
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
#
# Given an integer n, return true if n is an ugly number.
#
#
# Example 1:
#
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
#
# Input: n = 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
#
# Example 3:
#
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
#
# Example 4:
#
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求丑数，满足整数，只能被2、3、5整除。
# 直接循环判断是否可以整除2、3、5，若可以，就进行整除，直到得到1，或者不能整除。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 6')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isUgly(6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 8')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isUgly(8)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 14')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isUgly(14)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isUgly(1)))
    print()

    pass
# @lc main=end