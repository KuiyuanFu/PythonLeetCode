# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (36.99%)
# Likes:    450
# Dislikes: 769
# Total Accepted:    88.7K
# Total Submissions: 239.5K
# Testcase Example:  '28'
#
# A perfect number is a positive integer that is equal to the sum of its
# positive divisors, excluding the number itself. A divisor of an integer x is
# an integer that can divide x evenly.
#
# Given an integer n, return true if n is a perfect number, otherwise return
# false.
#
#
# Example 1:
#
#
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
#
#
# Example 2:
#
#
# Input: num = 6
# Output: true
#
#
# Example 3:
#
#
# Input: num = 496
# Output: true
#
#
# Example 4:
#
#
# Input: num = 8128
# Output: true
#
#
# Example 5:
#
#
# Input: num = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= num <= 10^8
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 完美整数，为其所有正除数的和。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 1

        for l in range(2, int(sqrt(num)) + 1):
            if num // l * l == num:
                s += l + num // l
        return s == num
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 28')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkPerfectNumber(28)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = 6')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkPerfectNumber(6)))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = 496')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkPerfectNumber(496)))
    print()

    print('Example 4:')
    print('Input : ')
    print('num = 8128')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkPerfectNumber(8128)))
    print()

    print('Example 5:')
    print('Input : ')
    print('num = 2')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().checkPerfectNumber(2)))
    print()

    pass
# @lc main=end